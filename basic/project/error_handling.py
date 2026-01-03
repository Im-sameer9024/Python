

x = ('masala','lemon','ginger')

y = enumerate(x)
print(list(y))

file = open('txt.py','r')

try:
    file.write('hello world')
finally:
    file.close()



with open('txt.py','r') as file:
    file.write('hello world')