from netmiko import ConnectHandler
from getpass import getpass



def inf_errors(output, interface, switch):
       
       link_status = output[0]['link_status']
       in_errors = output[0]['input_errors']
       out_errors = output[0]['output_errors']
       hostname = switch['host']
       
       
       print(f'DEVICE: {hostname}')
       print(f'INTERFACE: {interface}')
       print('*************************')
       print("Interface status: {}  ".format(link_status))       
       print("{} in_errors ".format(in_errors))
       print("{} out_errors ".format(out_errors) + '\n')



usr = input("Enter your Username: ")
passwrd = getpass()

vlc_dc2_n5k = ('vlc-dc02-acc-a', 'vlc-dc02-acc-b','vlc-dc02-acc-c', 'vlc-dc02-acc-d', 'vlc-dc02-acc-e', 'vlc-dc02-acc-f')
vlc_dc1_n5k = ('vlc-dc01-acc-a', 'vlc-dc01-acc-b', 'vlc-dc01-acc-e', 'vlc-dc01-acc-f')
bds_dc1_n5k_ab = ('bds-dc01-acc-a', 'bds-dc01-acc-b')
bds_dc1_n5k_cd = ('bds-dc01-acc-c', 'bds-dc01-acc-b')
bds_dc2_n5k_ab = ('bds-dc02-acc-a', 'bds-dc02-acc-b')
bds_dc2_n5k_cd = ('bds-dc02-acc-c', 'bds-dc02-acc-d')
bds_dc2_n5k_ef = ( 'bds-dc02-acc-e', 'bds-dc02-acc-f')
bds_dc2_n5k_gh = ( 'bds-dc02-acc-g', 'bds-dc02-acc-h')


#LIST OF N5K DEVICE GROUPS
dc_list = [vlc_dc2_n5k, vlc_dc1_n5k, bds_dc1_n5k_ab, bds_dc1_n5k_cd, bds_dc2_n5k_ab, bds_dc2_n5k_cd, bds_dc2_n5k_ef, bds_dc2_n5k_gh]


for dc_group in dc_list:
   if dc_group == dc_list[0] :
      interface = "port-channel3"
   elif dc_group == dc_list[1] :
      interface = "port-channel1"
   elif dc_group == dc_list[2] or dc_group == dc_list[-1] or dc_group == dc_list[-2] :
      interface = "port-channel123"   
   elif dc_group == dc_list[3] :
      interface = "port-channel125"
   elif dc_group == dc_list[4] :
      interface = "port-channel121"
   elif dc_group == dc_list[-3] :
      interface = "port-channel122"  
   for switch in dc_group:
     switch = {
        'device_type':'cisco_nxos',
        'host':switch,
        'username':usr, 
        'password':passwrd,
        'verbose':False
      }
     connection = ConnectHandler(**switch)
     command = ('show interface ' + interface)  
     output = connection.send_command(command, use_textfsm = True)
     inf_errors(output, interface, switch)
   
   
   
     
