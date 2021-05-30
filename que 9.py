list1=[21,16,2,3,55,66,44,5,8,0,9,]
b=[]
i=1
while i<len(list1):
    if list1[i]%2==0:
        b.append(list1[-i])
    i=i+1
print(b)










