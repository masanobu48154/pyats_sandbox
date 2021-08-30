#!user/bin/python

from genie import testbed
import pprint
import time
from logging import Formatter, getLogger, StreamHandler, DEBUG

logger = getLogger("genie_apis")
logger.setLevel(DEBUG)
handler = StreamHandler()
handler.setLevel(DEBUG)
fmt = Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "%Y-%m-%dT%H:%M:%S"
)
handler.setFormatter(fmt)
logger.addHandler(handler)
logger.propagate = False

testbed = testbed.load('testbed.yaml')

xe01 = testbed.devices['xe01']
xe02 = testbed.devices['xe02']

xe01.connect()
logger.debug("Successfully connected xe01!!")
xe02.connect()
logger.debug("Successfully connected xe01!!")

xe01_after_shut_status = xe01.api.get_interfaces_status()
xe02_after_shut_status = xe02.api.get_interfaces_status()

pprint.pprint(xe01_after_shut_status)
pprint.pprint(xe02_after_shut_status)

xe01.api.unshut_interface(interface='GigabitEthernet4')
logger.debug("Successfully unshuted xe01s' GigabitEthernet4")
xe02.api.unshut_interface(interface='GigabitEthernet2')
logger.debug("Successfully unshuted xe02s' GigabitEthernet2")
xe02.api.unshut_interface(interface='GigabitEthernet3')
logger.debug("Successfully unshuted xe02s' GigabitEthernet3")

time.sleep(10)

xe01_after_unshut_status = xe01.api.get_interfaces_status()
xe02_after_unshut_status = xe02.api.get_interfaces_status()

pprint.pprint(xe01_after_unshut_status)
pprint.pprint(xe02_after_unshut_status)

xe01.disconnect()
logger.debug("Successfully disconnected xe01!!")
xe02.disconnect()
logger.debug("Successfully disconnected xe02!!")
