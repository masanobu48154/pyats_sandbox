#!user/bin/python

from genie import testbed
import pprint
import time


def get_interfaces_status(device):
    """Get up/down status of all interfaces
    Args:
        device (obj): device object
    """

    try:
        out = device.parse('show ip interface brief')
    except SchemaEmptyParserError as e:
        log.error('No interface information found')
        return None

    # {'interface': {'GigabitEthernet1': {'interface_is_ok': 'YES',
    #           'ip_address': '172.16.1.210',
    #           'method': 'DHCP',
    #           'protocol': 'up',
    #           'status': 'up'},

    return {key: val.get('status') for key, val in out.get('interface', {}).items()}


testbed = testbed.load('testbed.yaml')
xe01 = testbed.devices['xe01']
xe02 = testbed.devices['xe02']

# unicon接続
xe01.connect()
xe02.connect()

# インターフェースのステータスを事前取得
xe01_before_shut_status = get_interfaces_status(xe01)
xe02_before_shut_status = get_interfaces_status(xe02)

# 事前取得したステータスを表示
print('-------xe01 interface status before shutdown-------')
pprint.pprint(xe01_before_shut_status)
print('---------------------------------------------------')
print('-------xe02 interface status before shutdown-------')
pprint.pprint(xe02_before_shut_status)
print('---------------------------------------------------')

# Apisを使ってxe01、xe02のインターフェースをshutdown
xe01.api.shut_interface(interface='GigabitEthernet4')
xe02.api.shut_interface(interface='GigabitEthernet2')
xe02.api.shut_interface(interface='GigabitEthernet3')

# ステータスがアップデートされるまでスリープ
time.sleep(20)

# インターフェースのステータスを事後取得
xe01_after_shut_status = get_interfaces_status(xe01)
xe02_after_shut_status = get_interfaces_status(xe02)

# 事後取得したステータスを表示
print('-------xe01 interface status after shutdown--------')
pprint.pprint(xe01_after_shut_status)
print('---------------------------------------------------')
print('-------xe02 interface status after shutdown--------')
pprint.pprint(xe02_after_shut_status)
print('---------------------------------------------------')

# unicon切断
xe01.disconnect()
xe02.disconnect()
