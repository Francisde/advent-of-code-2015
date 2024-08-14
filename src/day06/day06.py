
file1 = open('puzzle06.txt', 'r')
Lines = file1.readlines()

count = 0
def printGrid(grid):
    print("Print grid")
    for i in grid:
        print(i)

grid = [[0 for i in range(1000)] for i in range(1000)]
printGrid(grid)

for line in Lines:
    instruction = line.strip()
    print("Line {}: {}".format(count, instruction))
    if instruction.startswith("turn on"):
        instruction = instruction.replace("turn on ", "")
        coordinates = instruction.split(" through ")
        start_string = coordinates[0]
        end_string = coordinates[1]
        start_x = int(start_string.split(",")[0])
        start_y = int(start_string.split(",")[1])
        end_x = int(end_string.split(",")[0])
        end_y = int(end_string.split(",")[1])

        i = start_x

        while i <= end_x:
            j = start_y
            while j <= end_y:
                grid[i][j] +=1
                j += 1
            i += 1
    elif instruction.startswith("toggle"):
        instruction = instruction.replace("toggle ", "")
        coordinates = instruction.split(" through ")
        start_string = coordinates[0]
        end_string = coordinates[1]
        start_x = int(start_string.split(",")[0])
        start_y = int(start_string.split(",")[1])
        end_x = int(end_string.split(",")[0])
        end_y = int(end_string.split(",")[1])

        i = start_x

        while i <= end_x:
            j = start_y
            while j <= end_y:
                grid[i][j] += 2
                j += 1
            i += 1
    elif instruction.startswith("turn off"):
        instruction = instruction.replace("turn off ", "")
        coordinates = instruction.split(" through ")
        start_string = coordinates[0]
        end_string = coordinates[1]
        start_x = int(start_string.split(",")[0])
        start_y = int(start_string.split(",")[1])
        end_x = int(end_string.split(",")[0])
        end_y = int(end_string.split(",")[1])

        i = start_x

        while i <= end_x:
            j = start_y
            while j <= end_y:
                grid[i][j] = max(0, grid[i][j]- 1)
                j += 1
            i += 1

    count += 1

printGrid(grid)
lights_on = 0
for row in grid:
    for lamp in row:
        if lamp >= 0:
            lights_on += 1

brightness = 0
for row in grid:
    for lamp in row:
        brightness += lamp
print("TASK 1 - Lights on: {}".format(lights_on))

print("TASK 2 - Brightness: {}".format(brightness))
