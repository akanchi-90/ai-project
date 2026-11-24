x = int(input("what is x ?"))
y = int(input("what is y ?"))

if x > y or x < y :
    print("x is not y")
elif x == y :
    print("they are the same")

score = int(input("enter your score"))
if 90 <= score <= 100 :
    print("you got an A")
elif 80 <= score < 90:
    print("you got a B")
else :
    print("You got a C")

group = input("what is your group")

match group :
    case "ash" | "lam" | "bab" :
        print("agree")
    case "bas" | "lll":
        print("lol")
    case _ :
        print ("nope")