import requests

response = requests.get('https://randomuser.me/api/')
print(response)
data = response.json()
print(data)

a = 10 
b = 10

def add(a, b):
    return a + b 


c = add(1, 3)
print(c)
