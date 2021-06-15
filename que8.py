binary_number = [1, 0, 0, 1, 1, 0, 1, 1] 
i=0
sum=0
while i<len(binary_number):
    l=binary_number[-i-1]
    sum=sum+l*(2**i)
    i=i+1
print(sum)


# binary_number = [1, 0, 0, 1, 1, 0, 1, 1] 
# i=0
# a=0
# while binary_number!=0:
#     z=binary_number[-i-1]
#     a=a+z*(2**i)
#     i=i+1
# print(a)


# n=int(input("enter the decimal number"))
# l=[]
# z=0
# while(n!=0):
#     a=n%2
#     l.append(a)
#     n=n//2
# l.reverse()
# print(l)