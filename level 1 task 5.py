##Task: Palindrome Checker
##
##Write a Python function that checks whether
##a given string is a palindrome. A palindrome
##is a word, phrase, or sequence that reads the
##same backward as forward (e.g.,
##"madam" or"racecar").



def palidrome_checker(a):
    n=a[::-1]
    if a==n:
        print(a,"is palindrome.")
    else:
        print(a,"isnot palindrome.")


x=str(input("input:"))
palidrome_checker(x)
