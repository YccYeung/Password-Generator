# Password Generator
import random

def high_level(length):

    s = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+"
    t = ''.join(random.sample(s, length))
    pw = t.replace(" ", "")
    print(pw)

def low_level(length):

    number = random.randint(1,9)
    count = length
    while count != 0:
        pw = print(number,end='')
        number = random.randint(1,9)
        count -= 1

def level_check(lv):

    if lv == 'HIGH':
        print("you choose high level of password")
        return True
    if lv == 'LOW':
        print("you choose low level of password")
        return True
    if lv == "X":
        print("see you next time!")
        return True
    else:
        return False

def main():

    level = input("what level of password do you want? high or low? ")
    LEVEL = level.upper()

    while level_check(LEVEL) == False:

        print(f"{LEVEL} is not a valid input, please try again")
        level = input("what level of password do you want? high or low? ")
        LEVEL = level.upper()

    if LEVEL == "LOW":
        length = int(input("how long is your password: "))
        low_level(length)


    if LEVEL == "HIGH":
        length = int(input("how long is your password: "))
        high_level(length)


if __name__=='__main__':
    main()






