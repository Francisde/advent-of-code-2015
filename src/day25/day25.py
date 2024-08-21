def print_grid(input_grid):
    for row in input_grid:
        print(row)
    print()

def generate_code_grid(input_grid, start_value):
    input_grid[0][0] = start_value
    counter = 0
    current_x = 1
    last_start_x = current_x
    current_y = 0
    next_value = (start_value * 252533) % 33554393
    while current_x < len(input_grid):
        counter += 1
        input_grid[current_x][current_y] = next_value
        next_value = (next_value * 252533) % 33554393
        if current_x > 0:
            current_x -=1
            current_y +=1
        else:
            current_x = last_start_x + 1
            last_start_x = current_x
            current_y = 0



max_n = 10000

grid = [[0 for i in range(max_n)] for j in range(max_n)]




generate_code_grid(grid, 20151125)


print("TASK 1 - grid[][]: {}".format(grid[3009][3018]))

print("TASK 2 - ")
