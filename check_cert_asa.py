from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 



list_of_vpns =  [ 'dfs-vpn-51', 'dfs-vpn-01']
recipients = ['jesus.salvador@un.org']
#recipients = ['franqueza@un.org', 'nst-neg@un.org']

#usern = input('Username: ')
#passwd = getpass() 


for device in list_of_vpns:
    asa = {
      'device_type': 'cisco_asa',    
      'host': device,
      'username': 'cworks',
      'password': '',
      'secret': ''
      #'username': 'usern',     
      #'password': passwd,
      #'secret': passwd
    }
    print('*'*50 + '\n')
# Add date and time
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("date and time:",date_time)	
    print(f'opening connection to... {device}\n')
    print('sending commnands\n\n')
    net_connect = ConnectHandler(**asa)  
    net_connect.enable()
    output = net_connect.send_command('sh crypto ca certificates DFS_WC_2021 | grep end')
    net_connect.disconnect()

# Parse the command output and compare the date of the cert with current time
    all_fecher = output.split() 
    fecher = all_fecher[4:]
    comp_date = str(fecher[0] + ' ' + fecher[1]+ ' '+ fecher[2])
    date_end = datetime.strptime(comp_date, "%b %d %Y")
    today = datetime.today()
    days_2_go = (date_end - today).days
  
# Will send a mail if certificate is less than 31 till it expires    
    print(days_2_go)
    if days_2_go < 365: # will be modified to 31, used 365 for test purposes
          msg = MIMEMultipart()
          message = f'''
************************************************ 
*****Certificate expiration Notification: ******
************************************************

     Common name: *.dfs.un.org
     Expiration device: {device} 
     Certificate name: DFS_WC_2021 
     Expiration date: {date_end} 
     Days until expiration: {days_2_go}

         Comments:
            AOD must create the following WO's:
                WO1: #WAN WAAS Wildcard *.dfs.un.org certificate renewal.
                WO2: #DCC VPN Wildcard *.dfs.un.org certificate renewal.
                WO3: #DCC Script Check_cert_asa.py modification. The actions to be followed on this WO are the following:
                    1 - Diable crontab line to stop script from nsumgmt-51:
                        crontab -e 
                        Add #
                    2 - Modify script according new certificate name. 
                    3 - Restore crontab script iteration          
Thank you.
                    '''
 
          # setup the parameters of the message
          msg['From'] = "VPN_Certs@DPKO.UN.ORG"
          msg['To'] = ", ".join(recipients)
          msg['Subject'] = "This is a TEST: SSL certificate for *.dfs.un.org. ***WARNING: Expiration Notice"
          smtpServer='onesmtp.un.org'
          # Add in the message body
          msg.attach(MIMEText(message, 'plain'))
          # create server
          server = smtplib.SMTP(smtpServer,25)
          # send the message via the server.
          server.sendmail(msg['From'], recipients, msg.as_string())     
          server.quit()
          print ("successfully sent email to: " + msg['To'])


          



     
      




