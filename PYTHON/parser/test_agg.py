#!/usr/bin/python3
# SCRIPT TO PARSE INTERFACE AGGREGATION


from netmiko import ConnectHandler
import pprint
from device_test import devices
from jinja2 import Environment, FileSystemLoader 
import smtplib, email
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase




liste_parsed = []


def connect_device(device_name, int_list):
    try:
          
       switch = {
           'device_type':'cisco_nxos',
           'host':device_name,
           'username':'shownet', 
           'password':'234$Snwrk!!',
           'port':22,
           'verbose':True
        }
       print('*'*50 + '\n')
       print(f'opening connection to... {device_name} \n')
       print('sending commnands\n\n')
       net_connect = ConnectHandler(**switch)
       list_outs = []
       for intf in int_list:
           output = net_connect.send_command(f'show interface {intf}', use_textfsm = True)
           list_outs.append(output)
       net_connect.disconnect()
       print (list_outs)
    except:
        pass


interf = ['Ethernet10/15','Ethernet2/46']
connect_device('vlc-dc02-agg-a', interf)