def main():
    x,y,z = get_input().split()
    x = int(x)
    z = int(z)
    if y =="/" and z != 0 :
        print(f"{x / z :.1f}")
    if y =="/" and z == 0 :
        print("cannot divide by 0")  
    if y =="+"  :
         print(f"{x + z :.1f}")
def get_input():
    return input("expression ?  ")
    
main()