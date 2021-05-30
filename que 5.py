# # a=["n","i","t","i","p"]
# a=["m","o","m"]
# i=0
# j=len(a)-1
# while i<len(a):
#     if a[i]==a[j]:
#         i=i+1
#         j=j-1
#         print("it is palindrom")
#         break
#     else:
#         print("it not palindrom")
#         break

a=["n","i","t","i","n"]
b=[]
# length=len(a)
# print(length)
i=1
while i<=len(a):
    b.append(a[-i])
    i=i+1
print(b)
if b==a:
    print("it is a palindrome")
else:
    print("it is not palindrome")    

