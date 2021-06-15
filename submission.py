# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# a1=numbers[0]
# a2=max(numbers)
# print(a2)

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
largest=numbers
i=0
length=len(numbers)-1
while i<length:
    if numbers[i]>numbers[i+1]:
        numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
        print(numbers[-1])
    i=i+1


