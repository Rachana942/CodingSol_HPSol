import re

file1="/home/bharath/Rachana V/inputfile.txt"
file2="/home/bharath/Rachana V/inputfile2.txt"
file3="/home/bharath/Rachana V/inputfile3.txt"

def Employees(file):
    b=[]
    a=[]
    file = open(file, "r")
    for l in file:
        temp1=l.split()
        a.append(int(temp1[-1]))
        b.append(" ".join(temp1[:-1]))
    for i in range(1,len(a)):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                t1=a[i]
                a[i]=a[j]
                a[j]=t1
                t2 = b[i]
                b[i] = b[j]
                b[j] = t2
    print(a)
    print(b)
    min=999999
    for i in range(1,len(a)-a[0]-1):
        if(a[i+a[0]-1]-a[i]<min):
            min=a[i+a[0]-1]-a[i]
            c=i

    D=[]
    for x in range (c, c+a[0]):
        str1=b[x]+str(a[x])+"\n"
        D.append(str1)
        str1=""
    print(D)
    file2=open("/home/bharath/Rachana V/sample_output.txt","a")
    file2.write("The goodies selected for distribution are \n")
    for y in D:
        file2.write(y)
    str2="And the differene between the chosen with highest pay godie. and lower price is "+str(min)
    file2.write(str2)
    file2.write("\n")
    file2.write("\n")
        
Employees(file1)
Employees(file2)
Employees(file3)