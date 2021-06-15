elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum=0
sum1=0
while i<len(elements):
    if elements[i]%2==0:
        print(elements[i],"even")
        sum=sum+elements[i]
    else:
        print(elements[i],"odd")
        sum1=sum1+elements[i]
    i=i+1
print("evev",sum)
avg=sum/4
print(avg)
print("odd",sum1)
avg=sum1/7
print(avg)

