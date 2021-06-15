number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
l=[]
while i<len(n):
    b=4
    while b<len(n):
        if n[i]+n[b]==number:
            l.append([n[i],n[b]])
        b+=1
    i=i+1
print(l)


    