#!/usr/bin/env python3
"""Script for performing a backup of all files related to IWAN IOS CA server locally in dfs-ioscert-51. It then uploads that backup in dfs-neg-mgmt-52 server."""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from datetime import datetime, timezone
from settings import cworks_user, cworks_pwd, smtpServer, mail_from, mail_to
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import re
import smtplib

print('Step 0: Connecting to dfs-ioscert-51 server.')
host_ip = '10.130.94.122'

net_connect = Netmiko(host=host_ip, username=cworks_user, password=cworks_pwd, device_type="cisco_ios", global_delay_factor=4)
print(net_connect.find_prompt())

print('Step 1: Creating a backup of bootflash:/CA/ in dfs-ioscert-51 server bootflash:/CA_BACKUP/')
now = datetime.now()
date_backup = now.strftime("%H-%M-%S_%h_%d_%Y")
print(date_backup)
file_name = 'IWAN-IOS-CA-BACKUP-' + date_backup + '.tar'
print(file_name)
command = 'archive tar /create bootflash:/CA_BACKUP/' + file_name + ' bootflash:/CA/'
print(command)
output = net_connect.send_command(command)

print('Step 2: Copy this new backup in dfs-ioscert-01 router (secondary IOS CA)')

server_path = '/CA_BACKUP/' + file_name
print (server_path)
ioscert_bu_server = '10.130.222.131'

command = 'copy bootflash:/CA_BACKUP/' + file_name + ' scp:'
print("Sending command: " + command)
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False, delay_factor=4)
print(output)
if 'Address or name of remote host' in output:
    output = net_connect.send_command_timing(ioscert_bu_server, strip_prompt=False, strip_command=False, delay_factor=4)
    print(output)
    if 'Destination username' in output:
        output = net_connect.send_command_timing(net_connect.username, strip_prompt=False, strip_command=False, delay_factor=4)
        print(output)
        if 'Destination filename' in output:
            output = net_connect.send_command_timing(server_path, strip_prompt=False, strip_command=False, delay_factor=4)
            print(output)
            if 'Password' in output:
                output = net_connect.send_command_timing(net_connect.password, strip_prompt=False, strip_command=False, delay_factor=4)
                if 'bytes copied in' in output:
                    print("It seems backup has been uploaded in the IOS CERT backup server.")
                else:
                    raise ValueError("It seems the backup has not been uploaded in the IOS CERT backup server properly, please check it.")
            else:
                raise ValueError("Error while introducing user password of the server.")
        else:
            raise ValueError("Error while introducing destination filename.")
    else:
        raise ValueError("Error while introducing username.")
else:
    raise ValueError("Address or name of remote host not correct.")

def order_dates(bus_no_order):
    "This function receives a backup list and returns it ordered by date (first oldest)"
    dates = []   
    bu_order = []

    for i in bus_no_order :
        dates.append(datetime.strptime(i,"IWAN-IOS-CA-BACKUP-%H-%M-%S_%b_%d_%Y.tar"))
    dates.sort()    

    for d in dates:
        bu_order.append(d.strftime("IWAN-IOS-CA-BACKUP-%H-%M-%S_%b_%d_%Y.tar"))

    return bu_order;    

print('Step 3: Check if more than five backups are in place locally in the PRIMARY dfs-ioscert-51 router, if that is the case delete old ones.')    

command = 'dir bootflash:/CA_BACKUP/'
sh_dir = net_connect.send_command(command)
print(sh_dir)

bu_list = []
for line in sh_dir.splitlines():
    if 'IWAN-IOS-CA-BACKUP' in line:
        match = re.search(r"IWAN-IOS-CA-BACKUP-.*", line).group()
        bu_list.append(match)

print("Backup_list: ", bu_list)

bu_list_length = len(bu_list)
print('Current number of elements in bu_list: ', bu_list_length)

bu_list = order_dates(bu_list)

del_list = []
bu_list_2 = bu_list.copy()
for var in bu_list:
    if len(bu_list_2) > 7:
        del_list.append(var)
        bu_list_2.remove(var)

print("Backup_list: ", bu_list)
print("Backup_list_2: ", bu_list_2)
print("Delete_list: ", del_list)

print("Deleting old backups if more than five.")

for var in del_list:
    string1 = 'Delete filename [/CA_BACKUP/' + var +']'
    string2 = 'Delete bootflash:/CA_BACKUP/' + var
    print("String1: ", string1)
    print("String2: ", string2)
    command = 'delete bootflash:/CA_BACKUP/' + var
    print(command)
    output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False, delay_factor=4)
    if string1 in output:
        output = net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False, delay_factor=4)
        print(output)
        if string2 in output:
            output = net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False, delay_factor=4)
            print(output)
        else:
                raise ValueError("Error during second delete confirmation.")
    else:
        raise ValueError("Error during first delete confirmation.")

command = 'dir bootflash:/CA_BACKUP/'
sh_dir = net_connect.send_command(command)
print(sh_dir)
mssg_51 = sh_dir

net_connect.disconnect()

print('Step 4: Connect to dfs-ioscert-01 server')

net_connect = Netmiko(host=ioscert_bu_server, username=cworks_user, password=cworks_pwd, device_type="cisco_ios", global_delay_factor=4)
print(net_connect.find_prompt())

print('Step 5: Check if more than five backups are in place locally in the SECONDARY dfs-ioscert-01 router, if that is the case delete old ones.')  

command = 'dir bootflash:/CA_BACKUP/'
sh_dir = net_connect.send_command(command)
print(sh_dir)

bu_list = []
for line in sh_dir.splitlines():
    if 'IWAN-IOS-CA-BACKUP' in line:
        match = re.search(r"IWAN-IOS-CA-BACKUP-.*", line).group()
        bu_list.append(match)

print("Backup_list: ", bu_list)

bu_list_length = len(bu_list)
print('Current number of elements in bu_list: ', bu_list_length)

bu_list = order_dates(bu_list)

del_list = []
bu_list_2 = bu_list.copy()
for var in bu_list:
    if len(bu_list_2) > 7:
        del_list.append(var)
        bu_list_2.remove(var)

print("Backup_list: ", bu_list)
print("Backup_list_2: ", bu_list_2)
print("Delete_list: ", del_list)

print("Deleting old backups if more than five.")

for var in del_list:
    string1 = 'Delete filename [/CA_BACKUP/' + var +']'
    string2 = 'Delete bootflash:/CA_BACKUP/' + var
    print("String1: ", string1)
    print("String2: ", string2)
    command = 'delete bootflash:/CA_BACKUP/' + var
    print(command)
    output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False, delay_factor=4)
    if string1 in output:
        output = net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False, delay_factor=4)
        print(output)
        if string2 in output:
            output = net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False, delay_factor=4)
            print(output)
        else:
                raise ValueError("Error during second delete confirmation.")
    else:
        raise ValueError("Error during first delete confirmation.")

command = 'dir bootflash:/CA_BACKUP/'
sh_dir = net_connect.send_command(command)
print(sh_dir)
mssg_01 = sh_dir
net_connect.disconnect()


mssg_51_html = "<p>" + mssg_51.replace("\n","<br>") + "</p>"
mssg_01_html = "<p>" + mssg_01.replace("\n","<br>") + "</p>"


message = "<h1>IWAN-IOS-CA Backup Maintenance</h1>"

message += "<h4>CURRENT BACKUPS LIST OF DFS-IOSCERT-51 SERVER (PRIMARY SERVER)</h4>"

message += mssg_51_html

message += "<h4>CURRENT BACKUPS LIST OF DFS-IOSCERT-01 SERVER (SECONDARY SERVER)</h4>"

message += mssg_01_html

message_header = "<html><head><style>p {color:blue;} .bold {color:black; font-weight: bold;} table, th, td {border: 1px solid black; border-collapse: collapse;} th, td {padding: 5px;  text-align: left;} td.nok {background-color:#FF0000}</style></head><body>"
message_footer = "</body></html>"

complete_message = message_header + message + message_footer


server = smtplib.SMTP(smtpServer,25)
for recipient in mail_to:
 # create message object instance
 msg = MIMEMultipart()

 # setup the parameters of the message
 msg['From'] = mail_from
 msg['To'] = recipient
 msg['Subject'] = date_backup + " - Daily IWAN-IOS-CA Backup"


 # add in the message body
 msg.attach(MIMEText(complete_message, 'html'))

 try:
  server.sendmail(msg['From'], msg['To'], msg.as_string())
  print ("email successfully sent to " + msg['To'])
 except SMTPException as e:
  print("Error sending mail: %s" % e)
 except (socket.timeout,socket.error) as socketError:
  print("Unable to establish connection: %s" % socketError)
    
 msg = None

server.quit()
