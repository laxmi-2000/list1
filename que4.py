numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
while i<len(numbers):
    l=numbers[i]
    if l>numbers[0] and l<numbers[3]:
        print("second max",l)
    i=i+1