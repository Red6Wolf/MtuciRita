ip_list=[
    '10.1.1.1',
    '10.1.1.2',
    '10.1.1.3',
    '10.1.1.4',
    '10.1.1.5'
]

#1
print("Задание 1")
print("Первый элемент:", ip_list[0])
print("Последний элемент:", ip_list[-1])

#2
print("Задание 2")  # Заголовок задания 2.
ip_list.append('10.1.1.6')  # Добавление нового элемента в конец списка.
ip_list.extend(['10.1.1.55', '10.1.1.66'])  # Добавление нескольких элементов.

new_ip = ["172.16.1.1", "172.16.1.2", "172.16.1.3"]  # Создание списка новых IP-адресов.
ip_list += new_ip  # Добавление нового списка к существующему.
print(ip_list)  # Вывод обновленного списка.

print("Второй элемент", ip_list[1])  # Вывод второго элемента списка.
print("Предпоследний элемент", ip_list[-2])  # Вывод предпоследнего элемента списка.

ip_list.pop(0)  # Удаление первого элемента.
ip_list.pop(-1)  # Удаление последнего элемента.

ip_list[0] = '2.2.2.2'  # Изменение значения первого элемента.
print("Первый обновленный", ip_list[0])  # Вывод обновленного первого элемента.
print("Новый обновленный", ip_list)  # Вывод окончательного списка.


#3
print("Задание 3")  # Заголовок задания 3.
import random  # Импорт библиотеки для генерации случайных чисел.

acl_list = [random.randint(1, 119) for i in range(10)]  # Генерация списка случайных чисел.
print("Сгенерированый список", acl_list)  # Вывод сгенерированного списка.

acl_list.sort()  # Сортировка списка.
print("Отсортированный список", acl_list)  # Вывод отсортированного списка.

first_element = acl_list.pop(0)  # Извлечение первого элемента.
last_element = acl_list.pop(-1)  # Извлечение последнего элемента.
acl_list.insert(0, last_element)  # Добавление извлеченного последнего элемента в начало списка.
acl_list.append(first_element)  # Добавление извлеченного первого элемента в конец списка.
print("С заменой первого и последнего эллемента", acl_list)  # Вывод обновленного списка.

acl_list.reverse()  # Реверсирование списка методом `.reverse()`.
print("Список после реверса .reverse", acl_list)  # Вывод списка после реверса.

acl_list = acl_list[::-1]  # Реверсирование списка срезом.
print("Реверс при помощи среза", acl_list)  # Вывод списка после реверса срезом.

mid_index = len(acl_list) // 2  # Вычисление индекса середины списка.

acl_list1 = acl_list[:mid_index]  # Разделение списка на первую половину.
acl_list2 = acl_list[mid_index:]  # Разделение списка на вторую половину.
print('Первая половина списка', acl_list1)  # Вывод первой половины.
print('Вторая половина списка', acl_list2)  # Вывод второй половины.

#4
print('Задание 4')  # Заголовок задания 4.
user_input = input('Введите данные:')  # Ввод данных от пользователя.

list3 = [user_input]  # Создание списка из введенных данных.
print(list3)  # Вывод списка.

len_list3 = len(list3)  # Определение длины списка.
x = '1'  # Искомый символ.
count_x = sum(item.count(x) for item in list3)  # Подсчет числа вхождений символа `1`.
print('Длинна списка', len_list3)  # Вывод длины списка.
print('Сколько 1 в списке:', count_x)  # Вывод количества символов `1`.

#Задание 5
print('Задание 5')  # Заголовок задания 5.
ip_list = [  # Список IP-адресов с повторениями.
    '10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.2',
    '10.1.1.3', '10.1.1.1', '10.1.1.1', '10.1.1.2'
]

ip_addr_unique = set(ip_list)  # Преобразование списка в множество для удаления дубликатов.
print('Уникальные ip-адреса:', ip_addr_unique)  # Вывод уникальных IP.

ip_sorted = sorted(ip_addr_unique)  # Сортировка множества.
print('Отсортированный список уникалов', ip_sorted)  # Вывод отсортированного списка.

len_iplist = len(ip_addr_unique)  # Подсчет количества уникальных элементов.
print('Количество уникальных ip адресов', len_iplist)  # Вывод количества.
#6
print("Задание 6")  # Заголовок задания.

import random  # Импортируем модуль для генерации случайных чисел.
# Генерируем списки VLAN для Москвы, Курска и Новосибирска.
vlan_mos = [random.randint(1, 10) for i in range(8)]
vlan_kursk = [random.randint(1, 15) for i in range(10)]
vlan_novosib = [random.randint(1, 20) for i in range(15)]

# Выводим созданные списки VLAN для каждого города.
print("Созданные списки VLAN:",
      "\nМосква:", vlan_mos,
      "\nКурск:", vlan_kursk,
      "\nНовосибирск:", vlan_novosib)
# Определяем количество уникальных VLAN в Москве.
unique_vlans_mos = len(set(vlan_mos))
print("Количество уникальных VLAN в Москве:", unique_vlans_mos)

# Преобразуем списки VLAN в множества для удобного сравнения.
set_vlan_mos = set(vlan_mos)
set_vlan_kursk = set(vlan_kursk)
set_vlan_novosib = set(vlan_novosib)

# Выводим множества VLAN для каждого города.
print("Множество VLAN Москвы:", set_vlan_mos)
print("Множество VLAN Курска:", set_vlan_kursk)
print("Множество VLAN Новосибирска:", set_vlan_novosib)

# Находим общие VLAN между Москвой и Курском.
common_vlans_mos_kursk = set_vlan_mos.intersection(set_vlan_kursk)
print("Общие VLAN между Москвой и Курском:", common_vlans_mos_kursk)

# Находим общие VLAN во всех трех городах.
common_vlans_all = set_vlan_mos.intersection(set_vlan_kursk, set_vlan_novosib)
print("Общие VLAN во всех трех городах:", common_vlans_all)

# Определяем уникальные VLAN Новосибирска, которых нет в Москве и Курске.
unique_vlans_novosib = set_vlan_novosib - set_vlan_mos.union(set_vlan_kursk)
print("Уникальные VLAN в Новосибирске:", unique_vlans_novosib)

# Задание 7
print('Задание 7')  # Заголовок задания.

device = {  # Создаем словарь с информацией об устройстве.
    'ip': '10.10.10.12',  # IP-адрес устройства.
    'username': 'user',  # Имя пользователя.
    'password': 'pass',  # Пароль устройства.
}

print('Пароль устройства:', device['password'])  # Выводим пароль устройства.

device_key = list(device.keys())  # Получаем список ключей словаря.
device_value = list(device.values())  # Получаем список значений словаря.

print('Ключи устройства:', device_key)  # Выводим ключи устройства.
print('Значения устройства:', device_value)  # Выводим значения устройства.

add_config = {  # Новый словарь с дополнительной конфигурацией.
    'device_type': 'huawei',  # Тип устройства.
    'session_log': 'output.txt',  # Путь к файлу журнала сеанса.
}

device.update(add_config)  # Обновляем основной словарь, добавляя новые данные.
print('Обновленный словарь устройства:', device)  # Выводим обновленный словарь.

# Задание 8
print('Задание 8')  # Заголовок задания.

show_version = "   *0 CISCO881-SEC-K9 FTX0000038X   "  # Строка с данными о версии устройства.

show_version = show_version.strip()  # Убираем лишние пробелы по краям строки.

parts = show_version.split()  # Разбиваем строку на части по пробелам.
model = parts[1]  # Извлекаем модель устройства.
serial_number = parts[2]  # Извлекаем серийный номер устройства.

contains_cisco = 'cisco' in show_version.lower()  # Проверяем, есть ли в строке слово 'cisco'.
contains_881 = '881' in model  # Проверяем, содержится ли число '881' в модели устройства.

# Выводим серийный номер и модель устройства.
print(f"Серийный номер: {serial_number}, Модель устройства: {model}")

# Задание 9
print('Задание 9')  # Заголовок задания.

# Строки с информацией о MAC-адресах.
mac1 = "Internet 10.220.88.29 94 5254.abbe.5b7b ARPA FastEthernet4"
mac2 = "Internet 10.220.88.30 3 5254.ab71.e119 ARPA FastEthernet4"
mac3 = "Internet 10.220.88.32 231 5254.abc7.26aa ARPA FastEthernet4"

# Функция для извлечения IP-адреса и MAC-адреса из строки.
def extract_mac_ip(mac_entry):
    parts = mac_entry.split()  # Разделяем строку на части.
    ip_address = parts[1]  # Извлекаем IP-адрес.
    mac_address = parts[3]  # Извлекаем MAC-адрес.
    return ip_address, mac_address  # Возвращаем IP-адрес и MAC-адрес.

# Заголовок таблицы с выравниванием.
print(f"{'IP Address':<20} {'MAC Address':<20}")
print("-" * 40)  # Разделитель.

# Обрабатываем строки и выводим таблицу.
for mac in [mac1, mac2, mac3]:  # Проходим по всем строкам.
    ip, mac_addr = extract_mac_ip(mac)  # Извлекаем данные.
    print(f"{ip:<20} {mac_addr:<20}")  # Выводим IP и MAC в формате таблицы.

# Задание 10
print('Задание 10')  # Заголовок задания.

ip_input = input("Введите IP-адрес: ")  # Запрашиваем ввод IP-адреса у пользователя.

octets = ip_input.split('.')  # Разделяем IP-адрес на октеты.

# Обрабатываем каждый октет.
for i, octet in enumerate(octets, start=1):  # Нумеруем октеты, начиная с 1.
    decimal_value = int(octet)  # Преобразуем октет в целое число.
    binary_value = bin(decimal_value)[2:]  # Преобразуем октет в двоичное представление.
    hex_value = hex(decimal_value)  # Преобразуем октет в шестнадцатеричное представление.
    # Выводим информацию об октете в десятичном, двоичном и шестнадцатеричном формате.
    print(f"Octet {i}: {decimal_value} (Decimal), 0b{binary_value} (Binary), {hex_value} (Hexadecimal)")
