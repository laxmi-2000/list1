chr=[
    ['a','b','c','d','z'],
    ['e','f','g','h'],
    ['i','j','k'],
    ['m','n']
]
i=0
count=0
while i<len(chr):
    a=0
    while a<len(chr[i]):
        count=count+1
        a=a+1
    i=i+1
print(count)
