student=[23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
l= len(student)
i=0
less50=0
more50=0
while i<l:
    marks=student[i]
    if marks<50:
        less50 =less50+1
    else:
        more50=more50+1
    i=i+1
print("Marks more50: "+str(more50))
print("Marks less50: "+str(less50))


