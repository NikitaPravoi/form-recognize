import requests

url = 'http://127.0.0.1:5000/get_form'

# Тест 1: Подходящая форма MyForm
data1 = {'user_name': 'John Doe', 'order_date': '2023-01-01'}
response1 = requests.post(url, data=data1)
print(response1.text)  # Ожидаемый вывод: MyForm

# Тест 2: Подходящая форма PhoneForm
data2 = {'user_name': 'John Doe', 'phone': '+79320121993'}
response2 = requests.post(url, data=data2)
print(response2.text)  # Ожидаемый вывод: PhoneForm

# Тест 3: Подходящая форма OrderForm
data3 = {'user_name': 'Alice', 'lead_email': 'alice@example.com'}
response3 = requests.post(url, data=data3)
print(response3.text)  # Ожидаемый вывод: OrderForm

# Тест 4: Типизация полей
data4 = {'user_name': 'Bob', 'product_id': '12345', 'number': '+79320121993', 'secure_email': 'alice@example.com'}
response4 = requests.post(url, data=data4)
print(response4.json())
# Ожидаемый вывод: {'user_name': 'text', 'product_id': 'text', 'number': 'phone', 'secure_email': 'email'}

# Тест 5: Подходящая форма с дополнительным полем отсутствующим в форме
data5 = {'user_name': 'Bob', 'lead_email': 'alice@example.com', 'product_id': '12345'}
response5 = requests.post(url, data=data3)
print(response5.text)  # Ожидаемый вывод: OrderForm




