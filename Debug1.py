marks = [10, 32, 42, 65, 67, 89, 6, 38, 67]
total_marks = 0
counter = 0
while counter < len(marks):
    total_marks = total_marks + marks[counter]
    counter = counter + 1 
print("count:",counter)
print("total_marks:",total_marks)