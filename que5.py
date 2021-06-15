numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a=max(numbers[0],numbers[1])
second=min(numbers[4],numbers[4])
n=len(numbers)
i=0
while i>n:
    if numbers[i]>a:
        second=a
        a=numbers[i]
    elif numbers[i]>second and a != numbers[i]:
        second=numbers[i]
print("Second largest : ",str(second))


