
file1 = open('puzzle03.txt', 'r')
Lines = file1.readlines()

count = 0
visited_houses = []
current_location = (0,0)
visited_houses.append(current_location)
print(visited_houses)
for line in Lines:

    print("Line {}: {}".format(count, line.strip()))
    count += 1
    for character in line:
        if character == '>':
            new_location = (current_location[0], current_location[1] + 1)
            current_location = new_location
        elif character == '<':
            new_location = (current_location[0], current_location[1] - 1)
            current_location = new_location
        elif character == '^':
            new_location = (current_location[0] + 1, current_location[1])
            current_location = new_location
        elif character == 'v':
            new_location = (current_location[0] - 1, current_location[1])
            current_location = new_location

        if current_location not in visited_houses:
            visited_houses.append(current_location)


print("TASK 1 - Visited_Locations = {}".format(len(visited_houses)))

# Task 2

count = 0
visited_houses = []
current_location_santa = (0,0)
current_location_robo = (0,0)
visited_houses.append(current_location_santa)
print(visited_houses)
for line in Lines:

    print("Line {}: {}".format(count, line.strip()))

    for character in line:
        if count % 2 == 0:
            current_location = current_location_santa
        else:
            current_location = current_location_robo
        if character == '>':
            new_location = (current_location[0], current_location[1] + 1)
            current_location = new_location
        elif character == '<':
            new_location = (current_location[0], current_location[1] - 1)
            current_location = new_location
        elif character == '^':
            new_location = (current_location[0] + 1, current_location[1])
            current_location = new_location
        elif character == 'v':
            new_location = (current_location[0] - 1, current_location[1])
            current_location = new_location

        if current_location not in visited_houses:
            visited_houses.append(current_location)
        if count % 2 == 0:
            current_location_santa = current_location
        else:
            current_location_robo = current_location
        count += 1

print("TASK 2 - Visited_Locations = {}".format(len(visited_houses)))
