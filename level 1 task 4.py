##Create a Python program that acts as a basic
##calculator. It should prompt the user to
##enter two numbers and an operator (+, -,*, /,%),
##and then display the result of the
##operation.

def calculator(a):
    for i in range(0,len(a)):
        if a[i]=='*' or a[i]=='+' or a[i]=='-' or a[i]=='/' or a[i]=='%':
            op=a[i]
            break
        
    list=a.split(op)    
        
    if op=='*':
        print(a,'=',float(list[0])*float(list[1]))

    if op=='+':
        print(a,'=',float(list[0])+float(list[1]))
    if op=='-':
        print(a,'=',float(list[0])-float(list[1]))

    if op=='/':
        print(a,'=',float(list[0])/float(list[1]))

    if op=='%':
        print(a,'=',float(list[0])%float(list[1]))
    
x=str(input("equation:-"))
calculator(x)
