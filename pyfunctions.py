#use snake casing for function practice

#basic fucntion delaration and definition
def say_hello():
    print("hello")
    print('are')
    print('you')
#calling of defined fucntion
say_hello()


#parse parameters in the function
def say_hello_para(name):
    print(f'Hello {name}')

say_hello_para('Jay')

#assign deafult value if parameter is not passed
def say_hello_default(name = 'J'):
    print(f'Hello {name}')
#print a default value for name cause value not parsed
say_hello_default()


#returning a value in functions
def add_num(num1, num2):
    return num1+num2
#returning a value from a function
result = add_num(10, 20)
print(result)

