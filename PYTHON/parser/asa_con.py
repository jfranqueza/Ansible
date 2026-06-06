from netmiko import ConnectHandler
from getpass import getpass
# from datetime import datetime
from pprint import pprint
from netaddr import *
import pandas as pd
# import re
# import os
# import sys
# import socket

device_name = '10.130.90.253'

def connect_device(device_name):
    switch = {
        'device_type':'cisco_asa',
        'host':device_name,
        'username':'', 
        'password':'',
        'port':22,
        'verbose':True
    }
    print('*'*50 + '\n')
    print(f'opening connection to... {device_name} \n')
    print('sending commnands\n\n')
    net_connect = ConnectHandler(**switch)  
    net_connect.send_command('changeto sys')
    output = net_connect.send_command('show run | i context')
    listed_ouput = output.splitlines()
    # split1 = output.splitlines()
    # listed = []
    # for i in split1:
    #     split2 = i.splitlines()
    #     listed.append(split2)
    # print(output)
    net_connect.disconnect()
    return (listed_ouput)





def get_context(device_name):
    result = connect_device (device_name)
    # Get the list
    context_list = []
    for line in result:
        if line.startswith("context "):
            context_name = line.replace("context ", "")
            if context_name != "admin":
                context_list.append(context_name)
    return(context_list)


 
def get_rules(device, context_name):
    switch = {
        'device_type':'cisco_asa',
        'host':device_name,
        'username':'shownet', 
        'password':'234$Snwrk!!',
        "fast_cli": False,
        'port':22,
        'verbose':True
    }
    print('*'*50 + '\n')
    print(f'opening connection to... {device_name} \n')
    print('sending commnands\n\n')
    print(device)
    print(context_name)
    net_connect = ConnectHandler(**switch)  
    net_connect.send_command(f'changeto context {context_name}')
    list_rules = net_connect.send_command('show access-list', use_textfsm=True)
    # print(list_rules)
    return(list_rules)


def get_vlan_subnet(device, context_name):
    switch = {
        'device_type':'cisco_asa',
        'host':device_name,
        'username':'shownet', 
        'password':'234$Snwrk!!',
        "fast_cli": False,
        'port':22,
        'verbose':True
    }
    print('*'*50 + '\n')
    print(f'opening connection to... {device_name} \n')
    print('sending commnands\n\n')
    print(device)
    print(context_name)
    net_connect = ConnectHandler(**switch)  
    net_connect.send_command(f'changeto context {context_name}')
    list_subnets = net_connect.send_command('VCLOUD-UNMIK_V2071-out', use_textfsm=True)
    return(list_subnets)
     
     
 
# all_devices_contexts = []
# device_context = {}
devices = ['10.130.90.253']
# for i in devices:
#     on_device = get_context(i)
# print(on_device)
context_test = 'VCLOUD'

### GET ACL from CONTEXT #####
json_rules = get_rules(devices, context_test)
df = pd.DataFrame(json_rules)
df.to_csv('rules.csv')
print(df)

#### GET IP VLAN SUBNET #####
json_subnets = get_vlan_subnet(devices, context_test)
df = pd.DataFrame(json_rules)
df.to_csv('rules.csv')
pprint(json_subnets)
for dict in json_subnets:
    for k,j in dict.items():
        
        if k == 'description':
            vlan_name = j 
            print(vlan_name)
        elif k == 'ip_address':
            ip_adds = IPAddress(j)
        elif k == 'net_mask':
            ip_mask = IPAddress(j).netmask_bits()
    new_subnet = f'{ip_adds}/{ip_mask}'
    real_ip = ip.IPNetwork(new_subnet)
    new_vlan = [vlan_name, real_ip]
    print(new_vlan)
               

pprint(json_rules)


    device_context[i] = on_device
    all_devices_contexts.append(device_context)

    








