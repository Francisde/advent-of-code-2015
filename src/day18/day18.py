

file1 = open('puzzle18.txt', 'r')
Lines = file1.readlines()

def print_grid(grid):
    light_counter = 0
    for line in grid:
        for value in line:
            if value:
                print("#", end=' ')
                light_counter += 1
            else:
                print(".", end=' ')
        print()
    print("Lights on: {}".format(light_counter))

def perform_one_simulation_step(input_grid):
    new_grid = []
    for i in range(len(input_grid)):
        new_row = []
        for j in range(len(input_grid[i])):
            lights_on = 0
            try:
                if input_grid[i - 1][j - 1] and i > 0 and j > 0:
                    lights_on += 1
            except IndexError:
                pass
            try:
                if input_grid[i - 1][j] and i > 0:
                    lights_on += 1
            except IndexError:
                pass

            try:
                if input_grid[i - 1][j + 1] and i > 0:
                    lights_on += 1
            except IndexError:
                pass

            try:
                if input_grid[i][j + 1]:
                    lights_on += 1
            except IndexError:
                pass

            try:
                if input_grid[i + 1][j + 1]:
                    lights_on += 1
            except IndexError:
                pass

            try:
                if input_grid[i + 1][j]:
                    lights_on += 1
            except IndexError:
                pass

            try:
                if input_grid[i + 1][j - 1] and j > 0:
                    lights_on += 1
            except IndexError:
                pass

            try:
                if input_grid[i][j - 1] and j > 0:
                    lights_on += 1
            except IndexError:
                pass

            # try:
            #     if input_grid[i][j]:
            #         lights_on += 1
            # except IndexError:
            #     pass
            # print(lights_on)
            # print("i: {}, j:{}, lights: {}".format(i, j, lights_on))
            if input_grid[i][j]:
                if lights_on >= 2 and lights_on <= 3:
                    new_row.append(True)
                else:
                    new_row.append(False)
            else:
                if lights_on == 3:
                    new_row.append(True)
                else:
                    new_row.append(False)
        new_grid.append(new_row)
    new_grid[0][0] = True
    new_grid[0][len(new_grid[0]) - 1] = True
    new_grid[len(new_grid) - 1][len(new_grid[0]) - 1] = True
    new_grid[len(new_grid) - 1][0] = True
    return new_grid

count = 0
size = 100
steps = 100

grid = []
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    parsed_line = []
    for character in input_line:
        if character == "#":
            parsed_line.append(True)
        else:
            parsed_line.append(False)
    grid.append(parsed_line)

print_grid(grid)
# new_grid = perform_one_simulation_step(grid)
# print_grid(new_grid)
counter = 0
while counter < steps:
    grid = perform_one_simulation_step(grid)
    counter += 1
print_grid(grid)
print("TASK 1 - ")

print("TASK 2 - ")