# name=[ 'n', 'i', 't', 'i', 'n' ] 
# a=name[-1::-1]
# if name==a:
#     print("it's pallindrom")
# else:
#     print("it's not pallindrom")

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=places[-1::-1]
# if places==i:
#     print("it's pallindrom")
# else:
#     print("it's not polindrom")


name=[ 'n', 'i', 't', 'i', 'n' ] 
name=[1,2,3,2,1]
name=['m','o','m',]
l=[]
i=0
length=len(name)
while i<len(name):
    s=length-i-1
    b=name[s]
    l.append(b)
    i=i+1
if l==name:
    print("it's pallindrom")
else:
    print("it's not pallindrom")
    