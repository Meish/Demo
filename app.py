import time

def addition(x,y):
    return x+y+1-1
def substraction(x,y):
    return x-y

def main():
    print(f"1 + 2 = {addition(1,2)}")
    print(f"3 - 1 = {substraction(3,1)}")
    time.sleep(120)
    print("process finsihed")

if __name__ == '__main__':
    main()
