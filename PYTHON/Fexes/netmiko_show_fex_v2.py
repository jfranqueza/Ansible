

### SEND COMMANDS TO DEVICES


from netmiko import ConnectHandler
from getpass import getpass
import csv 



csv_file = 'show_fex.csv'
#create_file(csv_file, csv_columns)

with open('devices.txt') as f:
    devices = f.read().splitlines()







for device in devices:
   #print(device) 
   with open(csv_file) as f: 
      reader = csv.reader(f)
      next(reader, None)
      commands = []   
      for row in reader:
        #  print(device) 
        #  print(row[-1]) 
         if row[-1] == device:
            fex_command = (f'show interface {row[-2]}')
            commands.append(fex_command)
      print(commands)
       


#command = net_connect.send_command(f'show interface {row[-2]}')

    #   print(show_if )  




def change_fex_name(device_name, command_list):
    switch = {
        'device_type':'cisco_nxos',
        'host':device_name,
        'username':'franquezaj-su', #input("Enter your Username: ")
        'password':password,
        'port':22,
        'verbose':True
    }
    connection = ConnectHandler(**switch)  
    output = net_connect.send_config_set(command_list)
    

    
    

