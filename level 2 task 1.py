##Task: Guessing Game
##
##Write a Python program that generates a
##random number between 1 and 100. The
##user should then try to guess the number.
##The program should provide hints such as
##"too high" or "too low" until the correct
##number is guessed.



import random

def check(a):
    flag=0
    while flag==0:
        x=int(input("enter your number:"))
        if(x==a):
            flag=1
            print("finally matched with",a)
        else:
            if abs(x-a)<=10:
                print("too close")
            else:
                if x-a<0:
                    print("too low")
                else:
                    print("too high")

x=random.randint(1,100)
check(x)
