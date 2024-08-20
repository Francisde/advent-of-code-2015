

file1 = open('puzzle19.txt', 'r')
Lines = file1.readlines()

count = 0

replacements = []
input_molecule = ""

def get_all_replacements(input_string, replacement_list):
    result = set()
    for i in range(len(input_string)):
        for replacements_pair in replacement_list:
            if replacements_pair[0] == input_string[i]:
                result.add("{}{}{}".format(input_string[0:i], replacements_pair[1], input_string[i+1:]))
            elif len(replacements_pair) == 2 and  replacements_pair[0] == input_string[i:i+2]:
                result.add("{}{}{}".format(input_string[0:i], replacements_pair[1], input_string[i+2:]))
    return result

def get_all_replacements_reverse(input_string, replacement_list):
    result = set()
    for i in range(len(input_string)):
        for replacements_pair in replacement_list:
            # print("i: {}, replacement_pair: {}, input_string: {}".format(i, replacements_pair[1], input_string[i: i + len(replacements_pair[1]) ]))
            if replacements_pair[1] == input_string[i: i + len(replacements_pair[1]) ]:
                replacement = "{}{}{}".format(input_string[0:i], replacements_pair[0], input_string[i + len(replacements_pair[1]) :])
                if replacements_pair[0] == "e" and len(replacement) != 1:
                    continue
                # print("replacement: {}".format(replacement))
                result.add(replacement)
    return result

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    if "=>" in input_line:
        split_string = input_line.split(" => ")
        replacements.append((split_string[0], split_string[1]))
    else:
        input_molecule = input_line

print(replacements)
print(input_molecule)
solution_1 = get_all_replacements(input_molecule, replacements)
print(solution_1)
print("TASK 1 - possible replacements: {}".format(len(solution_1)))

# greedy algorithm
steps = 0
molecules = set()
molecules.add(input_molecule)
while "e" not in molecules and steps < 1000:
    set_after_this_round = set()
    longest = 0
    for molecule in molecules:
        new_molecules = get_all_replacements_reverse(molecule, replacements)
        for new_molecule in new_molecules:
            set_after_this_round.add(new_molecule)
            longest = max(longest, len(new_molecule))


    steps += 1
    molecules = set_after_this_round
    molecules_list = list(set_after_this_round)
    min = 488
    min_index = 0
    for i in range(len(molecules_list)):
        if len(molecules_list[i]) < min:
            min = len(molecules_list[i])
            min_index = i
    molecules = set()
    print(molecules_list)
    molecules.add(molecules_list[i])

    print("step: {}, number of combinations: {}, longest_comb: {}".format(steps, len(molecules), longest))

solution_2 = get_all_replacements_reverse("O", replacements)
print(solution_2)

print("TASK 2 - steps: {}".format(steps))
