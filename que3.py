# Code likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai unhe count kare. 
# Aur firr unka count print kare.

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# count=0
# l=[]
# while i<len(numbers):
#     if numbers[i]>20 and numbers[i]<40:
#         l.append(numbers[i])
#         count=count+1
#     i=i+1 
# print(l)
# print(count)


numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
count=0
while i<len(numbers):
    b=(numbers[i])
    if b>20 and b<40:
        count=count+1
        print(b)
    i=i+1
print(count)