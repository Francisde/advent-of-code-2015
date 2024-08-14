
file1 = open('puzzle01.txt', 'r')
Lines = file1.readlines()

count = 0
floor_count = 0
character_sent_santa_to_basement = 1
for line in Lines:

    print("Line {}: {}".format(count, line.strip()))
    count += 1
    for character in line.strip():
        if character == '(':
            floor_count += 1
        elif character == ')':
            floor_count -= 1
        if floor_count == -1:
            character_sent_santa_to_basement = count
            print("TASK 2 - Basement count: {}".format(character_sent_santa_to_basement))
        count += 1

print("TASK 1 - Final Floor: {}".format(floor_count))




