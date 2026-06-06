
import os
import sys
import csv
import json 

      
# ENTER CREDENTIALS

# user = input ("Introduce user: ")


# EXECUTE ANSIBLE COMMAND LINE

os.system("ansible-playbook pyats_2file_DC2_v2.yaml")

#os.system(f"ansible-playbook -u {user} -k pyats_2file_DC2_v2.yaml")
       
       

# FUNCTION TO CHECK INTERFACES ERRORS       
       
def inf_errors(file_json, interface, switch):
       
       crc = file_json[interface]['counters']['in_crc_errors']
       in_errors = file_json[interface]['counters']['in_errors']
       in_discard = file_json[interface]['counters']['in_discard']
       out_discard = file_json[interface]['counters']['out_discard']
       out_errors = file_json[interface]['counters']['out_errors']
       
       print(f'DEVICE: {switch}')
       print(f'INTERFACE: {interface}')
       print('*************************')
       print("{} CRC errors ".format(crc))
       print("{} in_errors ".format(in_errors))
       print("{} in_discard errors ".format(in_discard))
       print("{} out_discard errors ".format(out_discard))
       print("{} out_errors ".format(out_errors) + '\n')


# LIST OF VLC N5K DC02 DEVICES

vlc_dc2_n5k = { 'vlc-dc02-acc-a' : 'vlc-dc02-acc-a_interfaces.json', 
           'vlc-dc02-acc-b' : 'vlc-dc02-acc-b_interfaces.json', 
           'vlc-dc02-acc-c' : 'vlc-dc02-acc-c_interfaces.json',
           'vlc-dc02-acc-d' : 'vlc-dc02-acc-d_interfaces.json', 
           'vlc-dc02-acc-e' : 'vlc-dc02-acc-e_interfaces.json', 
           'vlc-dc02-acc-f' : 'vlc-dc02-acc-f_interfaces.json'
}


# LIST OF VLC N5K DC01 DEVICES

vlc_dc1_n5k = { 'vlc-dc01-acc-a' : 'vlc-dc01-acc-a_interfaces.json', 
           'vlc-dc01-acc-b' : 'vlc-dc01-acc-b_interfaces.json',  
           'vlc-dc01-acc-e' : 'vlc-dc01-acc-e_interfaces.json', 
           'vlc-dc01-acc-f' : 'vlc-dc01-acc-f_interfaces.json'
}


# LIST OF BDS N5K DC01 DEVICES

bds_dc1_n5k_ab = { 'bds-dc01-acc-a' : 'bds-dc01-acc-a_interfaces.json', 
           'bds-dc01-acc-b' : 'bds-dc01-acc-b_interfaces.json'
}
#PO 123
bds_dc1_n5k_cd = { 'bds-dc01-acc-a' : 'bds-dc01-acc-a_interfaces.json', 
           'bds-dc01-acc-b' : 'bds-dc01-acc-b_interfaces.json'
}
#PO 125


# LIST OF BDS N5K DC02 DEVICES

bds_dc2_n5k_ab = { 'bds-dc02-acc-a' : 'bds-dc02-acc-a_interfaces.json', 
           'bds-dc02-acc-b' : 'bds-dc02-acc-b_interfaces.json'
}
#PO121
bds_dc2_n5k_cd = { 'bds-dc02-acc-c' : 'bds-dc02-acc-c_interfaces.json', 
           'bds-dc02-acc-d' : 'bds-dc02-acc-d_interfaces.json'
}
#PO122
bds_dc2_n5k_ef = { 'bds-dc02-acc-e' : 'bds-dc02-acc-e_interfaces.json', 
           'bds-dc02-acc-f' : 'bds-dc02-acc-f_interfaces.json'
}
#PO123
bds_dc2_n5k_gh = { 'bds-dc02-acc-g' : 'bds-dc02-acc-g_interfaces.json', 
           'bds-dc02-acc-h' : 'bds-dc02-acc-h_interfaces.json'
}
#PO123

#LIST OF N5K DEVICE GROUPS
dc_list = [vlc_dc2_n5k, vlc_dc1_n5k, bds_dc1_n5k_ab, bds_dc1_n5k_cd, bds_dc2_n5k_ab, bds_dc2_n5k_cd, bds_dc2_n5k_ef, bds_dc2_n5k_gh]

#bds_dc_list = [bds_dc2_n5k_ab, bds_dc2_n5k_cd, bds_dc2_n5k_ef, bds_dc2_n5k_gh]
   

#LOOP FOR
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
      device_file = dc_group[switch]
      with open(device_file, 'r') as f:
         data_file = json.loads(f.read())
         #print('\nDevice: ', cnn3)
         check3 = inf_errors(data_file, interface, switch)
        
    

    
    
       
# for cnn3 in dc2_n5k:     
#    device_file = dc2_n5k[cnn3]
#    interface = 'port-channel3'  
#    with open(device_file, 'r') as f:
#       data_file = json.loads(f.read())
#       print('\nDevice: ', cnn3)
#       check3 = inf_errors(data_file, interface)



