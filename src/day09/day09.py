
from itertools import permutations

file1 = open('puzzle09.txt', 'r')
Lines = file1.readlines()

def calc_all_distances(city_list):
    shortest_distance = -1
    longest_distance = -1
    for permutation in permutations(city_list, len(city_list)):
        length = 0
        for j in range(len(permutation) - 1):
            length += distances["{}->{}".format(permutation[j], permutation[j + 1])]
        print(permutation)
        print(length)
        if shortest_distance == -1:
            shortest_distance = length
            longest_distance = length
        else:
            shortest_distance = min(shortest_distance, length)
            longest_distance = max(longest_distance, length)
    print(shortest_distance)
    print(longest_distance)
    return [shortest_distance, longest_distance]

count = 0
cities_list = []
distances = {}
# start Task one
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    distant_split = input_line.split(" = ")
    cities = distant_split[0].split(" to ")
    if cities[0] not in cities_list:
        cities_list.append(cities[0])
    if cities[1] not in cities_list:
        cities_list.append(cities[1])
    # parse distaces
    distances["{}->{}".format(cities[0], cities[1])] = int(distant_split[1])
    distances["{}->{}".format(cities[1], cities[0])] = int(distant_split[1])
print(cities_list)
print(distances)
distances_list = calc_all_distances(cities_list)

print("TASK 1 - Min Dist: {}".format(distances_list[0]))

print("TASK 2 - Max Dist: {}".format(distances_list[1]))
