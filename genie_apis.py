#!user/bin/python

from genie import testbed
import pprint

testbed = testbed.load('testbed.yaml')

xe01 = testbed.devices['xe01']
xe02 = testbed.devices['xe02']

xe01.connect()
xe02.connect()

xe01_before_shut_status = xe01.api.get_interfaces_status()
xe02_before_shut_status = xe02.api.get_interfaces_status()

pprint.pprint(xe01_before_shut_status)
pprint.pprint(xe02_before_shut_status)

xe01.api.shut_interface(interface='GigabitEthernet4')
xe02.api.shut_interface(interface='GigabitEthernet2')
xe02.api.shut_interface(interface='GigabitEthernet3')

xe01_after_shut_status = xe01.api.get_interfaces_status()
xe02_after_shut_status = xe02.api.get_interfaces_status()

pprint.pprint(xe01_after_shut_status)
pprint.pprint(xe02_after_shut_status)

xe01.api.unshut_interface(interface='GigabitEthernet4')
xe02.api.unshut_interface(interface='GigabitEthernet2')
xe02.api.unshut_interface(interface='GigabitEthernet3')

xe01_after_unshut_status = xe01.api.get_interfaces_status()
xe02_after_unshut_status = xe02.api.get_interfaces_status()

pprint.pprint(xe01_after_unshut_status)
pprint.pprint(xe02_after_unshut_status)

xe01.disconnect()
xe02.disconnect()
