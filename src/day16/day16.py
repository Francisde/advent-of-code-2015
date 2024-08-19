

file1 = open('puzzle16.txt', 'r')
Lines = file1.readlines()

facts = {}
facts["children"] = 3
facts["cats"] = 7
facts["samoyeds"] = 2
facts["pomeranians"] = 3
facts["akitas"] = 0
facts["vizslas"] = 0
facts["goldfish"] = 5
facts["trees"] = 3
facts["cars"] = 2
facts["perfumes"] = 1

count = 0

for line in Lines:
    input_line= line.strip()
    input_line = input_line.replace(":", "")
    input_line = input_line.replace(",", "")
    split_string = input_line.split(" ")
    index = int(split_string[1])
    key_1 = split_string[2]
    value_1 = int(split_string[3])
    key_2 = split_string[4]
    value_2 = int(split_string[5])
    key_3 = split_string[6]
    value_3 = int(split_string[7])
    fact_store = {}
    fact_list = [key_1, key_2, key_3]

    fact_store[key_1] = value_1
    fact_store[key_2] = value_2
    fact_store[key_3] = value_3
    hit = True
    for fact in fact_list:
        if fact == "cats" or fact == "trees":
            if facts[fact] >= fact_store[fact]:
                hit = False
                continue
        elif fact == "pomeranians" or fact == "goldfish":
            if facts[fact] <= fact_store[fact]:
                hit = False
                continue
        else:
            if facts[fact] != fact_store[fact]:
                hit = False
                continue

    if hit:
        print("Line {}: {}".format(count, input_line))
    count += 1
