from netmiko import ConnectHandler
from getpass import getpass
import csv 



# def create_file(csv_file, csv_columns):
#     with open (csv_file, 'w') as f:
#         writer =  csv.DictWriter(f, fieldnames=csv_columns)
#         writer.writeheader()              
#         # for data in output:
#         #     print(data)
#         #     writer.writerow(data)


# def add_data_2_file(file_name, columns_name, fex_output):
#     with open (file_name, 'a') as f:
#         writer =  csv.DictWriter(f, fieldnames=columns_name)
#         for data in fex_output:
#            print(data)
#            writer.writerow(data)


# ### FUNCTION TO READ THE CSV
# def read_csv(file_name, device_list):
#     for device in devices_list:
#        with open(file_name) as f: 
#          reader = csv.reader(f)
#          next(reader, None)
#          commands = []   
#          for row in reader:
#             #  print(device) 
#             #  print(row[-1]) 
#             if row[-1] == device:
#                 fex_command = (f'show interface {row[-2]}')
#                 commands.append(fex_command)
#          print(commands)
#          change_fex_name(device, commands)
     

## FUNCTION TO CHANGE NAME OF THE FEX WITH THE CSV        
# def change_fex_name(device_name, command_list):
#     switch = {
#         'device_type':'cisco_nxos',
#         'host':device_name,
#         'username':'franquezaj-su', #input("Enter your Username: ")
#         'password':password,
#         'port':22,
#         'verbose':True
#     }
#     connection = ConnectHandler(**switch)  
#     output = net_connect.send_config_set(command_list)
#     print(output)
 
            

# csv_columns = ['number', 'descr', 'state', 'model', 'serial', 'hostname']
# #csv_file = 'show_fex_'+router['host']+'.csv'
# #csv_columns = ['number', 'descr', 'state', 'model', 'serial']

# csv_file = 'show_fex.csv'
# #create_file(csv_file, csv_columns)  #Call to function to create original csv file



with open('devices_vlc.txt') as f:
    devices = f.read().splitlines()
print(devices)

password = getpass()
#input("Enter your Username: ") #Ask for user name as var
 
for device in devices:
    switch = {
        'device_type':'cisco_nxos',
        'host':device,
        'username':'franquezaj-su', # Name var could be retrieved
        'password':password,
        'port':22,
        'verbose':True
    }
    connection = ConnectHandler(**switch)  
    output = connection.send_command('show ip interface brief"', use_textfsm = True)
    # lista_dicts=[]
    # for d in output:
    #     d['hostname']=switch['host']
    #     lista_dicts.append(d)
    print(output)
    
    # add_data_2_file(csv_file, csv_columns, lista_dicts)
    # #read_csv(csv_file, lista_dicts)
    
    
    
    print('Closing connection')
    connection.disconnect()












### ONE CSV PER DEVICE
# for device in devices:
#     switch = {
#         'device_type':'cisco_nxos',
#         'host':device,
#         'username':'franquezaj-su', #input("Enter your Username: ")
#         'password':password,
#         'port':22,
#         'verbose':True
#     }
#     connection = ConnectHandler(**switch)  
#     output = connection.send_command('show fex', use_textfsm = True)
#     lista_dicts=[]
#     for d in output:
#         d['hostname']=switch['host']
#         lista_dicts.append(d)
#     print(lista_dicts)
#     add_data_2_file(csv_file, csv_columns, lista_dicts)
#     print('Closing connection')
#     connection.disconnect()








