# binary_number = [1, 0, 0, 1, 1]
binary_number = [1, 0, 0, 1, 1, 0, 1]  
i=0
sum=0
l=len(binary_number)
while i<len(binary_number):
    num=binary_number[l-i-1]
    sum=sum+num*(2**i)
    i=i+1
print(sum)