

file1 = open('puzzle20.txt', 'r')
Lines = file1.readlines()

count = 0

puzzle_input = 0
house_limit = 10000000
houses = [0 for i in range(house_limit)]


for line in Lines:
    input_line= line.strip()
    puzzle_input = int(input_line)
for i in range(house_limit):
    if i != 0:
        presents_per_house = i * 11
        current_house = i
        visited_houses = 0
        while current_house < house_limit:
            houses[current_house] += presents_per_house
            current_house += i
            visited_houses += 1
            if visited_houses == 50:
                break

index_greater_than = 0
for i in range(len(houses)):
    print("House {}, presents: {}".format(i, houses[i]))
    if houses[i] > puzzle_input and index_greater_than == 0:
        index_greater_than = i

print("TASK 1 - lowest house number: {}".format(index_greater_than))

print("TASK 2 - ")
