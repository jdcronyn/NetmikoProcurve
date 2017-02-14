import netmiko
from datetime import datetime
import getpass

#device_IP = raw_input("Enter IP of device: ")
device_username = raw_input("Enter username: ")
device_password = getpass.getpass("Enter password: ")

####Define devices####



hp_procurve1 = {
    'device_type': 'hp_procurve',
    'ip':   "",
    'username': device_username,
    'password': device_password,
    'verbose': False,
}
hp_procurve2 = {
    'device_type': 'hp_procurve',
    'ip':   "",
    'username': device_username,
    'password': device_password,
    'verbose': False,
}


#### List of all devices ####

all_devices = [hp_procurve1,hp_procurve2]

#### List of commands to run ####

commands = [
	"sh run".
	"wr mem"
] 

#### List of config commands to run####		

# Uncomment to update device configuration Comment to disable config update. Part1/2.
#Comment start
config = [
	"vlan 50",
	"name Testing"
]
#Comment end

#### Start of session loop ####

start_time = datetime.now()

#### Connection handler loop ####

for devices in all_devices:
	SSHClass = netmiko.ssh_dispatcher(device_type="hp_procurve")
	net_connect = SSHClass(**devices)
	
	#Comment start
	net_connect.send_config_set(config)	# Uncomment to update device configuration. Comment to disable config update. Part2/2.
	#Comment end
	#### Execution loop ####
	
	
	for command in commands:
		net_connect.enable()
		
		output = net_connect.send_command(command)
		print output

	end_time = datetime.now()
	total_time = end_time - start_time 

print total_time