
# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ] 
# i=0
# sum=0
# sum1=0
# sum2=0
# while i<len(magic_square):
#     colum=0
#     row=0
#     diag=0
#     while i<len(magic_square):
#         sum=sum+magic_square[i][colum]
#         sum1=sum1+magic_square[i][row]
#         sum2=sum2+magic_square[i][diag]z
#         colum=colum+1
#         row=row+1
#         diag=diag+1
#     i=i+1
# print(sum)
# print(sum1)
# print(sum2)
# if sum==sum1==sum2:
#     print("it's magic_square")
# else:
#     print("it's not magic_square")


# magic_square = [
#     [8, 4, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ] 
# i=0
# sum1=0
# while i<len(magic_square):
#     col=0
#     while col<len(magic_square):
#         sum1=sum1+magic_square[i][col]
#         break
#     i=i+1
# print(sum1)
# b=0
# sum2=0
# while b<len(magic_square):
#     row=0
#     while row<len(magic_square):
#         sum2=sum2+magic_square[b][row]
#         break
#     b=b+1
# print(sum2)
# d=0
# sum3=0
# while d<len(magic_square):
#     dig=0
#     while dig<len(magic_square):
#         sum3=sum3+magic_square[d][dig]
#         break
#     d=d+1
# print(sum3)
# if sum1==sum2==sum3:
#     print("it's magic square")
# else:
#     print("it's not magic square")
         
magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
l=0
sum=0
while l<len(magic_square):
    col=0
    while col<len(magic_square):
        sum=sum+magic_square[l][col]
        break
    b=0
    sum1=0
    while b<len(magic_square):
        row=0
        while row<len(magic_square):  
            sum1=sum1+magic_square[b][row]
            break
        b=b+1
    d=0
    sum2=0
    while d<len(magic_square):
        dig=0
        while dig<len(magic_square):
            sum2=sum2+magic_square[d][dig]
            break
        d=d+1
    l=l+1
print(sum)
print(sum1)
print(sum2)
if sum==sum1==sum2:
    print("it's magic square")
else:
    print("it's not magic square")


