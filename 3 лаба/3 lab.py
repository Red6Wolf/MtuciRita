# Задание 1
print('Задание 1')
with open("devices.txt", "r") as file:
    for line in file:
        print(line.strip())
# Задание 2
print('Задание 2')
with open("devices.txt", "r") as file:
    for line in file:
        if line.strip():
            print(line.strip())
# Задание 3
print('Задание 3')
list_devices = []
with open("devices.txt", "r") as file:
    for line in file:
        list_devices.append(line.strip())
print(list_devices)

# Задание 4
print('Задание 4')
with open("devices.txt", "r+") as file:
    content = file.readlines()
    file.seek(0)
    file.write("New start line\n")
    file.writelines(content)
    file.write("\nNew end line\n")
with open("devices.txt", "r") as file:
    print(file.read())

# Задание 5
print('Задание 5')
vlan_data = []
with open("show_vlan.txt", "r") as file:
    for line in file:
        if "VLAN" in line:
            parts = line.split()
            vlan_data.append((parts[0], parts[1]))
print(vlan_data)

# Задание 6
print('Задание 6')
with open("show_arp.txt", "r") as file:
    for line in file:
        parts = line.split()  

        # Проверяем, что строка содержит как минимум 4 элемента (IP и MAC адресы)
        if len(parts) >= 4:
            ip_addr = parts[1]  # Извлекаем IP-адрес из второго элемента
            mac_addr = parts[3]  # Извлекаем MAC-адрес из четвертого элемента

            # Выводим извлеченные IP и MAC адреса
            print(f"IP: {ip_addr}, MAC: {mac_addr}")

# Задание 7: Поиск заданных IP-адресов в ARP таблице
print('Задание 7')
# Открываем файл show_arp.txt в режиме чтения
with open("show_arp.txt", "r") as file:
    for line in file:  # Читаем файл построчно
        parts = line.split()  # Разбиваем строку на части по пробелам

        # Проверяем, что строка содержит как минимум 4 элемента (IP и MAC адресы)
        if len(parts) >= 4:
            ip_addr = parts[1]  # Извлекаем IP-адрес из второго элемента
            mac_addr = parts[3]  # Извлекаем MAC-адрес из четвертого элемента

            # Проверяем, совпадает ли IP с 10.220.88.1 (шлюз по умолчанию)
            if ip_addr == "10.220.88.1":
                print(f"IP/MAC шлюза по умолчанию: IP = {ip_addr}, MAC = {mac_addr}")
                break  # Прерываем цикл, как только найдено

            # Проверяем, совпадает ли IP с 10.220.88.30 (устройство Arista 3)
            if ip_addr == "10.220.88.30":
                print(f"Arista 3 IP/MAC is: IP = {ip_addr}, MAC = {mac_addr}")
                break  # Прерываем цикл, как только найдено

# Задание 8: LLDP данные
print('Задание 8')
with open("show_lldp_neighbors_detail.txt", "r") as file:
    for line in file:  # Читаем файл построчно
        if "System Name" in line:  # Если в строке есть "System Name"
            system_name = line.split(":")[1].strip()  # Извлекаем значение
        if "Port id" in line:  # Если в строке есть "Port id"
            port_id = line.split(":")[1].strip()  # Извлекаем значение
        if "System Name" in line and "Port id" in line:  # Убедимся, что обе переменные найдены
            break  # Выходим из цикла после извлечения нужных данных

# Выводим результат
print(f"Имя системы: {system_name}, ID Порта: {port_id}")

# Задание 9
print('Задание 9')
# Импортируем модуль json и функцию pprint для форматированного вывода
import json
from pprint import pprint

# Открываем файл interface_config.json и читаем содержимое
with open("interface-config.json", "r") as file:
    json_text = file.read()  # Читаем файл как текст

# Выводим тип данных переменной json_text
print(f"Тип переменной json_text: {type(json_text)}")

# Выводим содержимое переменной json_text
print("Содержимое json_text:")
print(json_text)

# Преобразуем JSON-формат в объект Python
json_data = json.loads(json_text)

# Выводим тип данных переменной json_data
print(f"\nТип переменной json_data: {type(json_data)}")

# Форматированный вывод содержимого json_data
print("\nСодержимое json_data:")
pprint(json_data)

# Задание 10
print('Задание 10')
import json
from pprint import pprint

# Открываем файл interfaces.json и читаем его содержимое
with open("interfaces.json", "r") as file:
    json_data = json.load(file)  # Парсим JSON в Python объект

# Проверяем наличие ключа "ietf-interfaces:interfaces" и вложенного "interface"
if "ietf-interfaces:interfaces" in json_data:
    interfaces = json_data["ietf-interfaces:interfaces"].get("interface", [])
    # Проходим по всем интерфейсам
    for interface in interfaces:
        name = interface.get("name", "N/A")  # Имя интерфейса
        ipv4 = interface.get("ietf-ip:ipv4", {}).get("address", [{}])  # Данные IPv4
        ip = ipv4[0].get("ip", "N/A")  # IP-адрес
        netmask = ipv4[0].get("netmask", "N/A")  # Маска сети
        # Выводим информацию об интерфейсе
        print(f"Интерфейс: {name}, IP-адрес: {ip}, Маска: {netmask}")
else:
    print("Ключ 'ietf-interfaces:interfaces' отсутствует в JSON.")

# Задание 11: Работа с JSON данными
print('Задание 11')
import json
from pprint import pprint  # Импортируем функцию pprint для «красивого» вывода данных

# Открываем файл interfaces.json и читаем его
with open("interfaces.json", "r") as file:
    json_data = json.load(file)  # Парсим JSON в объект Python

# Проверяем наличие корректного ключа
if "ietf-interfaces:interfaces" in json_data:
    # Получаем все интерфейсы из JSON данных
    interfaces = json_data["ietf-interfaces:interfaces"].get("interface", [])

    # Печать всех интерфейсов
    pprint(interfaces)  # Печать всех данных из списка интерфейсов в «красивом» формате
else:
    print("Ключ 'ietf-interfaces:interfaces' отсутствует в JSON.")

# Задание 12: Работа с YAML
print('Задание 12')
import yaml  # Импортируем модуль YAML

with open("yaml_int1.yml", "r") as file:  # Открываем YAML файл
    yaml_data = yaml.safe_load(file)  # Читаем содержимое
print(yaml_data)  # Выводим данные YAML
print('13')
import yaml
from pprint import pprint

# Открываем YAML файл и читаем его содержимое
with open("lab11_2_yaml.yml", "r") as file:
    data = yaml.safe_load(file)

# Выводим данные на экран с помощью print
print("Результат с использованием print:")
print(data)

# Выводим данные в "красивом" виде с помощью pprint
print("\nРезультат с использованием pprint:")
pprint(data)
