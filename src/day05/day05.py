
file1 = open('puzzle05.txt', 'r')
Lines = file1.readlines()
vovevls = ["a", "e", "i", "o", "u"]
bad_sequences = ["ab", "cd", "pq", "xy"]
count = 0
nice_strings = 0
for line in Lines:
    naughty = False
    #print("Line {}: {}".format(count, line.strip()))
    count += 1
    for seq in bad_sequences:
        if seq in line:
            print("{} - naughty".format(line.strip()))
            naughty = True
            break
    vovel_count = 0
    for character in line.strip():
        if character in vovevls:
            vovel_count +=1
    if vovel_count < 3:
        print("{} - naughty".format(line.strip()))
        naughty = True
        continue
    has_double_char = False
    for i in range(0, len(line.strip()) - 1):
        if line[i] == line[i + 1]:
            has_double_char = True
    if not has_double_char:
        naughty = True
        print("{} - naughty".format(line.strip()))
        continue

    if not naughty:
        print("{} - nice".format(line.strip()))
        nice_strings += 1


print("TASK 1 - number of nice strings = {}".format(nice_strings))


# part 2
nice_strings = 0
for line in Lines:
    rule_1 = False
    rule_2 = False

    # check for rule 1 - not overlapping pairs
    for i in range(0, len(line.strip()) - 3):
        sequence = line[i:i+2]
        last_index = line.rfind(sequence)
        if last_index >= i + 2:
            rule_1 = True

    # check for rule 2 - one letter with one between
    for i in range(0, len(line.strip()) - 2):
        if line[i] == line[i + 2]:
            rule_2 = True



    print("string: {}, rule 1: {}, rule 2: {}".format(line.strip(), rule_1, rule_2))
    if rule_1 and rule_2:
        nice_strings += 1

print("TASK 2 - number of nice strings = {}".format(nice_strings))