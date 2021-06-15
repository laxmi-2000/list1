elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
count=0
sum=0
while i<len(elements):
    sum=sum+elements[i]
    count=count+1
    i=i+1
print("it's count:" ,count)
print("it's sum:" ,sum)
avg=sum/11
print("avg:-",avg)

# i=0
# a=0
# b=0
# count=0
# count1=0
# while i<len(elements):
#     if elements[i]%2==0:
#         print(elements[i],"even")
#         a=a+elements[i]
#         count=count+1
#     else:
#         print(elements[i],"odd")
#         b=b+elements[i]
#         count1=count1+1
#     i=i+1
# print(count,"it is even",a)
# avg=a/4
# print(avg)
# print(count1,"it is odd",b)
# avg=b/7
# print(avg)


    

