from itertools import combinations


def get_all_possible_batches(list_of_presents, weight):
    results = []
    for i in range(len(list_of_presents)):
        print(i)
        added = False

        combination_list = list(combinations(list_of_presents, i))
        for comb in combination_list:
            comb_sum = 0
            for element in list(comb):
                comb_sum += element
            if comb_sum == weight:
                results.append(list(comb))
                added = True
            elif comb_sum < weight:
                added = True
        if not added and results != []:
            print("break cause no new package was added")
            break
    return list(results)


file1 = open('puzzle24.txt', 'r')
Lines = file1.readlines()

count = 0

presents = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    presents.append(int(input_line))

weight_sum = 0
for present in presents:
    weight_sum += present
print(weight_sum)
max_sum_per_batch = int(weight_sum /4)
print(max_sum_per_batch)

batches = get_all_possible_batches(presents, max_sum_per_batch)
print(len(batches))

group_1 = []
min_length = 100
for batch in batches:
    min_length = min(min_length, len(batch))
for batch in batches:
    if len(batch) == min_length:
        group_1.append(batch)
print("min batches: {}".format(len(group_1)))
min_quantum = -1
# calc quantum
for batch in group_1:
    quantum = 1
    for entry in batch:
        quantum *= entry
    print("batch: {}, QE = {}".format(batch, quantum))
    if quantum < min_quantum or min_quantum == -1:
        min_quantum = quantum
print("min quantum: {}".format(min_quantum))

first_group = []
for batch in group_1:
    quantum = 1
    for entry in batch:
        quantum *= entry
    if quantum == min_quantum:
        first_group = batch
        break


new_present_list = []
for present in presents:
    if present not in first_group:
        new_present_list.append(present)
distinct_batches_from_group_1 = get_all_possible_batches(new_present_list, max_sum_per_batch)

print("Distinct batches: {}".format(len(distinct_batches_from_group_1)))


print("TASK 1 - ")

print("TASK 2 - ")
