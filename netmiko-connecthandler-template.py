from netmiko import ConnectHandler

cisco_device = {
    'device_type': '[device type]',
    'host': '[ip address]',
    'username': '[username]',
    'password': '[password]',
    'secret': '[enable password]',
}

ssh = ConnectHandler(**cisco_device)
