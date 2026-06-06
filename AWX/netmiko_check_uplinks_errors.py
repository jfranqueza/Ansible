from netmiko import ConnectHandler
from os import environ
import smtplib
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
import getpass
#from getpass import getpass



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



#usr = environ.get('YOUR_USER')
#passwrd = environ.get('YOUR_PASS')

# vlc_dc2_n5k = ('vlc-dc02-acc-a', 'vlc-dc02-acc-b','vlc-dc02-acc-c', 'vlc-dc02-acc-d', 'vlc-dc02-acc-e', 'vlc-dc02-acc-f')
# vlc_dc1_n5k = ('vlc-dc01-acc-a', 'vlc-dc01-acc-b', 'vlc-dc01-acc-e', 'vlc-dc01-acc-f')
bds_dc1_n5k_ab = ('bds-dc01-acc-a', 'bds-dc01-acc-b')
# bds_dc1_n5k_cd = ('bds-dc01-acc-c', 'bds-dc01-acc-d')
# bds_dc2_n5k_ab = ('bds-dc02-acc-a', 'bds-dc02-acc-b')
# bds_dc2_n5k_cd = ('bds-dc02-acc-c', 'bds-dc02-acc-d')
# bds_dc2_n5k_ef = ( 'bds-dc02-acc-e', 'bds-dc02-acc-f')
# bds_dc2_n5k_gh = ( 'bds-dc02-acc-g', 'bds-dc02-acc-h')


#LIST OF N5K DEVICE GROUPS
#dc_list = [vlc_dc2_n5k, vlc_dc1_n5k, bds_dc1_n5k_ab, bds_dc1_n5k_cd, bds_dc2_n5k_ab, bds_dc2_n5k_cd, bds_dc2_n5k_ef, bds_dc2_n5k_gh]
dc_list = [bds_dc1_n5k_ab]

for dc_group in dc_list:
   # if dc_group == dc_list[0] :
   #    interface = "port-channel3"
   # elif dc_group == dc_list[1] :
   #    interface = "port-channel1"
   # elif dc_group == dc_list[2] or dc_group == dc_list[-1] or dc_group == dc_list[-2] :
   #    interface = "port-channel123"   
   if dc_group == dc_list[0] :
      interface = "port-channel123"
   # elif dc_group == dc_list[4] :
   #    interface = "port-channel121"
   # elif dc_group == dc_list[-3] :
   #    interface = "port-channel122"  
   for switch in dc_group:
     switch = {
        'device_type':'cisco_nxos',
        'host':switch,
        'username':'user', 
        'password':'pass',
        'verbose':False
      }
     connection = ConnectHandler(**switch)
     command = ('show interface ' + interface)  
     output = connection.send_command(command, use_textfsm = True)
     inf_errors(output, interface, switch)
     connection.disconnect()  #afegit per mi
     
     
     
     
### nya[a
# 

now = datetime.now()
date_backup = now.strftime("%H-%M-%S_%h_%d_%Y")



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


server = smtplib.SMTP(dfs-smtp.dfs.un.org,25)
for recipient in mail_to:
 # create message object instance
 msg = MIMEMultipart()

 # setup the parameters of the message
 msg['From'] = jonas@un.org
 msg['To'] = franqueza@un.org
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
