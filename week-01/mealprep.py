def main():
    x= input("what time is it now ? ")
    
    print(convert(x))

def convert(time):
    x,y = time.split(":")
    x = int(x)
    y = float(int(y)/60)
    return float(x + y)
if __name__ == "__main__":
    main()
