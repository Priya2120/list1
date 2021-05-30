# Code likho jo iss list mein se maximum dhund kar ke print kare.

num=[50,40,23,70,56,12,5,10,7]
largest=num[0]
i=0
while i<len(num):
    if num[i]>largest:
        largest=num[i]
    i=i+1
print(largest)