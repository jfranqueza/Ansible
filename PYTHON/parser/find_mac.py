from netmiko import ConnectHandler
from getpass import getpass
import pprint

def connect_device(device_name):
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
    output = net_connect.send_command('show mac address-table', use_textfsm = True)
    net_connect.disconnect()
    return (output)

 
list_of_macs = ['72f1.e480.002c','72f1.e480.002d','72f1.e480.006a','72f1.e480.006b','72f1.e480.0046','72f1.e480.0047','72f1.e480.0052','72f1.e480.0053','72f1.e480.0056','72f1.e480.0057',
                '72f1.e480.005a','72f1.e480.005b','72f1.e480.005e','72f1.e480.0062']

pp = pprint.PrettyPrinter(indent=4)

with open('devices_bds.txt') as f:
   devices = f.read().splitlines()

for device in devices:
     mac_table = connect_device (device)
     for mac in list_of_macs:
          for mc in mac_table:
            if mc['mac'] == mac:
              port = mc['ports']    
              print (f'MAC {mac} found in {port} of device {device}')
     
      



