# NAPALM en NXOS es basura
#### punto  #####


#from netmiko import ConnectHandler
from napalm import get_network_driver
from getpass import getpass
import json


passwd = getpass(prompt='Password: ', stream=None)

driver = get_network_driver('nxos_ssh')
optional_args = { 'port': 22}
ios = driver('10.130.88.73', 'franquezaj-su', passwd, optional_args=optional_args)
ios.open()

output=ios.get_interfaces_counters()
print(output)


# print(output['Ethernet0/0']['rx_errors'])


ios.close()

#for item, value in output:
#  print(item[value])

#dump = json.dumps(output, sort_keys=True, indent=4)
#print(dump)