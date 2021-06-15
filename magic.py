magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
i=0
sum1=0
while i<len(magic_square):
    col=0
    while i<=len(magic_square):
        sum1=sum1+magic_square[i][col]
        break
    i=i+1
print(sum1)
b=0
sum2=0
while b<=len(magic_square):
    row=0
    while b<len(magic_square):
        if b==row:
            sum2=sum2+magic_square[b][row]
            break
        row=row+1
    b=b+1
print(sum2)
d=0
sum3=0
while d<=len(magic_square):
    dig=0
    while d<len(magic_square):
        if d==dig:
            sum3=sum3+magic_square[d][dig]
            break
        dig=dig+1
    d=d+1
print(sum3)
if sum1==sum2==sum3:
    print("it's magic square")
else:
    print("it's not magic square")


