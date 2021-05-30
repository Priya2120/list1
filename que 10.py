a=int(input("enter the number :"))
b=str(a)
l=len(b)
t=l-1
i=0
while i<len(b):
    priya=int(b[i])
    num=(priya)*10**t
    print(num,end=" ")
    if i!=len(b)-1:
        print("+",end=" ")
    i=i+1
    t=t-1