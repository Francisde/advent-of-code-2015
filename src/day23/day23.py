

file1 = open('puzzle23.txt', 'r')
Lines = file1.readlines()

count = 0
instructions = []

# parse programm
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    split_line = input_line.split(" ")
    instructions.append(split_line)



# simulate program
register_a = 1
register_b = 0
next_instruction_pointer = 0
while True:
    if next_instruction_pointer < 0 or next_instruction_pointer >= len(instructions):
        break
    next_instruction = instructions[next_instruction_pointer]
    if next_instruction[0] == "inc":
        if next_instruction[1] == "a":
            register_a += 1
        else:
            register_b += 1
        next_instruction_pointer +=1
    elif next_instruction[0] == "tpl":
        if next_instruction[1] == "a":
            register_a *= 3
        else:
            register_b *= 3
        next_instruction_pointer +=1
    elif next_instruction[0] == "hlf":
        if next_instruction[1] == "a":
            register_a /= 2
        else:
            register_b /= 2
        next_instruction_pointer +=1
    elif next_instruction[0] == "jmp":
        next_instruction_pointer += int(next_instruction[1])
    elif next_instruction[0] == "jie":
        if next_instruction[1] == "a,":
            if register_a % 2 == 0:
                next_instruction_pointer += int(next_instruction[2])
            else:
                next_instruction_pointer +=1
        else:
            if register_b % 2 == 0:
                next_instruction_pointer += int(next_instruction[2])
            else:
                next_instruction_pointer +=1
    elif next_instruction[0] == "jio":
        if next_instruction[1] == "a,":
            if register_a == 1:
                next_instruction_pointer += int(next_instruction[2])
            else:
                next_instruction_pointer +=1
        else:
            if register_b  == 1:
                next_instruction_pointer += int(next_instruction[2])
            else:
                next_instruction_pointer +=1


print("TASK 1 - register a: {}, register b: {}".format(register_a, register_b))

print("TASK 2 - ")
