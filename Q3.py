students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
length=len(students)
# print(len(students))
# print(len(marks))
i=0
counter = 0
while i < length:
    print(students[counter] + str(marks[counter]))
    counter=counter+1