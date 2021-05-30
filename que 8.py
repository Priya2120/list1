list1=[3,4,5,6,7,8,9,10,44,33,55,77,99,45]
b=[]
i=1
while i<len(list1):
    if list1[i]%2!=0:
        b.append(list1[i])
    i=i+1
print(b)
