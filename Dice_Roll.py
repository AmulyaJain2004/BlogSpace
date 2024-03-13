import time
import random 

def main():
    while (True):
        on_click = bool(int(input("roll the dice: ")))
        if on_click == True:
            number = random.randint(1,6)
            time.sleep(1) 
            print (number)
        else:
            break
        if number != 6:
            break
    return 0

if __name__ == "__main__":
    main()
