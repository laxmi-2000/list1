money=[
    [12,65,88,55,77,44],
    [90,84,234,9876,12]
]
i=0
sum=0
count=0
while i<len(money):
    j=0
    while j<len(money[i]):
        sum=sum+money[i][j]
        count=count+1
        j=j+1
    i=i+1
print(count)
print(sum)
avg=sum/9
print(avg)