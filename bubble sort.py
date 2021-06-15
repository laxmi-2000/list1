lax=[8, 2, 4, 1, 3, 5, 9, 11, 10, 7]
i=0
print(lax)
while i<len(lax):
    l=0
    while l<i:
        if lax[i]<lax[l]:
            s=lax[i]
            lax[i]=lax[l]
            lax[l]=s
        l=l+1
    i=i+1
print(lax)



