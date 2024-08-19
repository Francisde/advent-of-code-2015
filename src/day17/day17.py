from itertools import combinations
from itertools import permutations
import math
file1 = open('puzzle17.txt', 'r')
Lines = file1.readlines()

count = 0
containers = []
right_combinations = {}

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    containers.append(input_line)
    right_combinations[str(count)] = 0

possible_combinations = 0
min_number_of_container = len(containers)
for i in range(len(containers) + 1):
    list_of_combinations = list(combinations(containers, i))
    print(list_of_combinations)
    for combination in list_of_combinations:
        sum_size = 0
        for container in combination:
            sum_size += int(container)
        if sum_size == 150:
            possible_combinations += 1
            min_number_of_container = min(min_number_of_container, len(combination))
            right_combinations[str(len(combination))] = right_combinations[str(len(combination))] + 1

print("TASK 1 - possible combinations: {}".format(possible_combinations))

print("TASK 2 - min number containers: {}, ways to fill them up: {}".format(min_number_of_container, right_combinations[str(min_number_of_container)]))