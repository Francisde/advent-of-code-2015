
file1 = open('test.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:

    print("Line {}: {}".format(count, line.strip()))
    count += 1


print("TASK 1 - ")

print("TASK 2 - ")