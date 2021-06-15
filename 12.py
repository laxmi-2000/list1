chr=['z','b','s','d','l','p','n','j','a']
i=0
print(chr)
while i<len(chr):
    n=0
    while n<i:
        if chr[i]<chr[n]:
            s=chr[i]
            chr[i]=chr[n]
            chr[n]=s
        n=n+1
    i=i+1
print(chr)




