from itertools import permutations
file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

def calc_max_happiness(attendee_list):
    max_happiness = 0
    for permutation in permutations(attendee_list, len(attendee_list)):
        happiness = 0
        for i in range(len(permutation)):
            if i == len(permutation) - 1:
                happiness += happiness_dict["{}->{}".format(permutation[i], permutation[0])]
                happiness += happiness_dict["{}->{}".format(permutation[0], permutation[i])]
            else:
                happiness += happiness_dict["{}->{}".format(permutation[i], permutation[i + 1])]
                happiness += happiness_dict["{}->{}".format(permutation[i + 1], permutation[i])]
        max_happiness = max(max_happiness, happiness)

    return max_happiness

count = 0
attendees = []
happiness_dict = {}
for line in Lines:
    input_line= line.strip()
    input_line = input_line.replace(".", "")
    print("Line {}: {}".format(count, input_line))
    count += 1
    split_string = input_line.split(" ")
    if split_string[0] not in attendees:
        attendees.append(split_string[0])
    if split_string[2] == "lose":
        happiness_dict["{}->{}".format(split_string[0], split_string[10])] = 0 - int(split_string[3])
    else:
        happiness_dict["{}->{}".format(split_string[0], split_string[10])] = int(split_string[3])

max_happiness = calc_max_happiness(attendees)
print("TASK 1 - max happiness: {}".format(max_happiness))

# add me
for attendee in attendees:
    happiness_dict["{}->{}".format(attendee, "me")] = 0
    happiness_dict["{}->{}".format("me", attendee)] = 0

attendees.append("me")

max_happiness = calc_max_happiness(attendees)
print("TASK 2 - max happiness with me: {}".format(max_happiness))
