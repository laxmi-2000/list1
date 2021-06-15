# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ] 

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ] 

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
i=0
sum=0
while i<len(marks):
    s=0
    while s<len(marks[i]):
        sum=sum+marks[i][s]
        s=s+1
    i=i+1
print(sum)
avg=sum/17
print(avg)

# i=0
# count=0
# while i<len(marks):
#     s=0
#     sum=0
#     a=0
#     while s<len(marks[i]):
#         a=a+marks[i][s]
#         s=s+1
#     sum=sum+a
#     avg=sum/len(marks[i])
#     i=i+1
#     count=count+1
#     print(count,"year avg=",avg)


