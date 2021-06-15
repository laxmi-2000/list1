elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum=0
sum2=0
while i<len(elements):
    if elements[i]%2==0:
        print(elements[i],"even")
        sum=sum+elements[i]
    else:
        print(elements[i],"odd")
        sum2=sum2+elements[i]
    i=i+1
print("evev",sum)
print("odd",sum2)
