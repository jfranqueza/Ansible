from netmiko import ConnectHandler
import getpass



dc_group = ['bds-dc02-acc-c', 'bds-dc02-acc-d']
commands = ['Show hardware internal carmel', 'Show hardware internal carmel logs both', 'Show hardware internal carmel logs event', 'Show hardware internal carmel all-ports', 'Show hardware internal carmel all-ports detail', 'Show hardware internal', 'carmel event-history msgs', 'Show hardware internal carmel event-history errors', 'Show system internal kernel messages', 'Show system internal kernel nvram-trace']

passwd = getpass.getpass()

for device in dc_group:
    switch = {
        'device_type':'cisco_nxos',
        'host':device,
        'username':'shownet', 
        'password': passwd,
        'verbose':False
    }
    connection = ConnectHandler(**switch)
    print(f'connecting to {device}')
    
    for command in commands:
        print('*'*50)
        print(f'Sending command {command}')
        output = connection.send_command(command)
        name = f'{command}_{device}.txt'
        with open (name, 'w') as f:
            data = output
            f.write(data)
    connection.disconnect()  
    
    