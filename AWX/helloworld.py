from os import environ

name = environ.get('YOUR_NAME')
passwd = environ.get('YOUR_PASS')
print(f'hola {name}')
print(passwd)