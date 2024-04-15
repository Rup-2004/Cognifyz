##Task: File Manipulation
##
##Write a Python program that reads a text
##file and counts the occurrences of each
##word in the file. Display the results in
##alphabetical order along with their
##respective counts.

def counter():
    file1=open('texttoread.txt','r')
    content=file1.read()

    for i in range(0,95):
        count=content.count(chr(32+i))
        
        if count==0:
            continue
        if i==0 :
            print("[space]\t",count)
        else:
            print(chr(32+i),"\t",count)

   
counter()
