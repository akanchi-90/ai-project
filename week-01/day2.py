x = input("what's x ?")
y = input ("whats y?")
z = int(x)+int(y)
print(z)
a=int(input("what is a?"))
b=int(input("what is b?"))
print (f"{a+b:,}")
price = 1234.5
print(f"Total: ${price:,.4f}")
print(f"{1234567:,}")    # 1,234,567
def hello(to="world"):
    print("hello,",to)
q=input("what name?")
hello(q)
name = input("your name? ")
print(name.upper())
print(name.title())
print(len(name))
print(type(name))
x = 10          # global: made at the top level of the file

def show():
    print(x)    # ✅ the function can READ it

show()          # 10
print(x)        # 10
def greet():
    message = "hello"   # local: only exists inside greet()
    print(message)

greet()          # hello

count = 0

def add_one():
    global count     # "I mean the global count"
    count = count + 1

add_one()
add_one()
print(count)   # 2
