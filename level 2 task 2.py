##Task: Number Guesser
##
##Create a number guessing game where the
##program generates a random number
##between a specified range, and the user tries
##to guess it. Provide feedback to the user if
##their guess is too high or too low.


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

i=int(input("Enter the lower range:-"))
j=int(input("Enter the upper range:-"))

x=random.randint(i,j)
check(x)
