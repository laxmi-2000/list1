magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 8]
] 
sum=0
i=0
while i<len(magic_square):
    colum=0
    while i<len(magic_square):
        sum=sum+(magic_square)[i][colum]
        # break
        colum=colum+1
    i=i+1
print(sum)
j=0
sum1=0
while j<len(magic_square):
    row=0
    while j<len(magic_square):
        sum1=sum1+magic_square[j][row]
        # break
        row=row+1
    j=j+1
print(sum1)
l=0
sum2=0
while l<len(magic_square):
    diag=0
    while l<len(magic_square):
        sum2=sum2+magic_square[l][diag]
        # break
        diag=diag+1
    l=l+1
print(sum2)
    # i=i+1
# print(sum)
# print(sum1)
# print(sum2)
if sum==sum1==sum2:
    print("it's magic square")
else:
    print("it's not magic square")


