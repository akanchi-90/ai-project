# ============================================
# DAY 2 QUIZ: write your guess, THEN run
# ============================================

print("----- EASY -----")

# Q1
print(7 // 2, 7 % 2, 7 / 2)
# Guess:3.1,1,3.1

# Q2
print(int("8") + int(2.9))
# Guess:10

# Q3
print(round(4.567, 1))
# Guess:4.6

# Q4
print(type(10 / 2))
# Guess:float

# Q5
name = "python"
print(name.upper(), len(name))
# Guess:PYTHON 6

# Q6
def double(n):
    return n * 2

print(double(4) + 1)
# Guess:9

# Q7
print(f"{1500000:,}")
# Guess:1,500,000


print("----- TRICKY -----")

# T1
print(round(0.5), round(1.5), round(2.5))
# Guess:0,1,2

# T2
print(2 ** 3 ** 2)
# Guess:64

# T3
print(-2 ** 2)
# Guess:4

# T4
print("5" + "5", "5" * 3)
# Guess:55,15

# T5
def say_hi():
    print("hi")

x = say_hi()
print(x)
# Guess:null

# T6
count = 10

def bump(count):
    count = count + 5
    return count

bump(count)
print(bump(count))
# Guess:15

# T7
def check(n):
    if n > 0:
        return "positive"
        print("this line?")
    return "not positive"

print(check(5), check(0))
# Guess:Positive,not Positive

# T8
print(int(-3.7), round(-3.7))
# Guess:-3,-4

# T9
print(0.1 + 0.2 == 0.3)
# Guess:true

# T10
print(f"{2.5:.0f}", f"{3.5:.0f}")
# Guess:2,3


print("----- ERROR ROUND -----")
# Each of these CRASHES. Uncomment ONE at a time.
# Guess the error type (TypeError, ValueError, NameError...) and WHY.

# E1
#print(int(input("Age: ")) + 25)
# Guess:

# E2
int(3.5)
# Guess:4

# E3
# score = 5
# def add_point():
#     score = score + 1
# add_point()
# Guess:

# E4
# def greet():
#     msg = "hello"
# greet()
# print(msg)
# Guess:
