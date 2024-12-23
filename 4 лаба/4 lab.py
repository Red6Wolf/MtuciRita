# Задание 1
print('Задание 1')

# Создаем функцию ssh_conn с тремя параметрами
def ssh_conn(ip_address, username, password):
    print(f"IP Address: {ip_address}")
    print(f"Username: {username}")
    print(f"Password: {password}")


ssh_conn('192.168.1.1', 'admin', 'admin123') # Вызов функции с позиционными аргументами
ssh_conn(ip_address='10.0.0.1', username='user1', password='password123') # Вызов функции с именованными аргументами
ssh_conn('172.16.0.1', password='secure_pass', username='root') # Вызов функции с сочетанием позиционных и именованных аргументов

# Задание 2
print('Задание 2')

# Создаем функцию ssh_conn2 с дополнительным параметром device_type
def ssh_conn2(ip_address, username, password, device_type='huawei_vrp'):
    print(f"IP Address: {ip_address}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Device Type: {device_type}")

ssh_conn2('192.168.1.2', 'admin', 'admin123', device_type='cisco_ios')
ssh_conn2('192.168.1.3', 'user', 'user123')

params = {
    'ip_address': '10.10.10.1',
    'username': 'test_user',
    'password': 'test_password',
    'device_type': 'juniper_junos'
}
ssh_conn2(**params)

# Задание 3
print('Задание 3')
import random

def generate_ip(octets='192.168.1'):
    last_octet = random.randint(1, 254)
    return f"{octets}.{last_octet}"

print(generate_ip())
print(generate_ip('10.0.0'))
print(generate_ip(octets='172.16.0')) # Вызов функции с именованным аргументом

# Задание 4
print('Задание 4')

nums = [45, 36, 39, 37, 130, 105, 220, 169]
divisible_by_13 = list(filter(lambda x: x % 13 == 0, nums))
print(divisible_by_13)

# Задание 5
print('Задание 5')

user_input = []
while True:
    value = input("Введите значение (или 'end' для завершения): ")
    if value.lower() == 'end':
        break
    user_input.append(value)

filtered = list(filter(lambda x: x.isalpha(), user_input))
print(filtered)

# Задание 6
print('Задание 6')

import re

with open("show_version.txt", "r") as file:
    data = file.read()

version = re.search(r"Version\s+(\S+)", data).group(1)
serial = re.search(r"Processor board ID\s+(\S+)", data).group(1)
register = re.search(r"Configuration register is\s+(\S+)", data).group(1)

print(f"IOS Version: {version}")
print(f"Serial Number: {serial}")
print(f"Configuration Register: {register}")

# Задание 7
print('Задание 7')

model = re.search(r'Cisco (?P<model>\d+)', show_version).group('model')
memory = re.search(r'(?P<memory>\d+K/\d+K bytes)', show_version).group('memory')

print(f"Model: {model}")
print(f"Memory: {memory}")

# Задание 8
print('Задание 8')

with open('show_ipv6_intf.txt', 'r') as file:
    content = file.read()

ipv6_addresses = re.findall(r'([0-9a-fA-F:]+/\d+)', content)
filtered_ipv6 = [addr for addr in ipv6_addresses if addr.startswith('2001')]

print(filtered_ipv6)

# Задание 9
print('Задание 9')

def validate_password(password):
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return True
    return False

while True:
    password = input("Введите пароль: ")
    if validate_password(password):
        print(f"Пароль успешно создан: {password}")
        break
    else:
        print("Пароль не соответствует требованиям. Попробуйте снова.")
