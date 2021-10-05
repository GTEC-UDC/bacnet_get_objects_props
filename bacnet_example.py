# Example
#
# Connect to a BACnec device and get the list of its available objects (points).
# Once we have the list of objects we can obtain their properties, for example
# the address, the type, the current value, etc.

import BAC0

# IP address of bacnet device
device_ip = '10.18.24.54'

bacnet = BAC0.lite()

# get device ID of controller in given IP
info = bacnet.whois(device_ip)[0]
# info = (device_ip, 11)

# create device object
dev = BAC0.device(info[0], info[1], bacnet, poll=0)

# list device points
# dev.points

# create dictionary of names to points
points_dic = {point.properties.name:point for point in dev.points}

# read properties of a point of interest
point_name = 'Informatica_CL_Radon'
point = points_dic[point_name]
point.properties

# {'device': INFORMATICA / Connected,
#  'name': 'Informatica_CL_Radon',
#  'type': 'analogInput', 'address': '18',
#  'description': '', 'units_state': 'becquerels',
#  'simulated': (False, 0), 'overridden': (False, 0),
#  'priority_array': None, 'history_size': None,
#  'bacnet_properties': {}}

# value of the point of interest
point.value

# address and type of the point of interest
paddr = point.properties.address # '18'
ptype = point.properties.type # 'analogInput'

# the point value can be obtained from the type and address with
bacnet.read(device_ip + ' ' + ptype + ' ' + paddr + ' presentValue')
