
file1 = open('puzzle07.txt', 'r')
Lines = file1.readlines()

count = 0

wires = {}
print(wires)
for line in Lines:
    print("Line {}: {}".format(count, line.strip()))
    count += 1

# get start input values
instructions_to_do = []
for line in Lines:
    input_line = line.strip()
    if input_line.split(" -> ")[0].isnumeric():
        wires[input_line.split(" -> ")[1]] = int(input_line.split(" -> ")[0])
    else:
        instructions_to_do.append(input_line)
print(wires)
print(instructions_to_do)
while len(instructions_to_do) != 0:
    current_instructions = instructions_to_do
    instructions_to_do = []
    print(wires)

    for instruction in current_instructions:
        if "AND" in instruction:
            operands = instruction.split(" -> ")[0]
            input_operands = operands.split(" AND ")
            output_operand = instruction.split(" -> ")[1]
            if input_operands[0] in wires and input_operands[1] in wires:
                wires[output_operand] = wires[input_operands[0]] & wires[input_operands[1]]
            elif input_operands[0] == "1" and input_operands[1] in wires:
                wires[output_operand] = 1 & wires[input_operands[1]]
            else:
                if instruction == "b AND n -> p":
                    print("cant do: {}".format(instruction))
                instructions_to_do.append(instruction)
        elif "OR" in instruction:
            operands = instruction.split(" -> ")[0]
            input_operands = operands.split(" OR ")
            output_operand = instruction.split(" -> ")[1]
            if input_operands[0] in wires and input_operands[1] in wires:
                wires[output_operand] = wires[input_operands[0]] | wires[input_operands[1]]
            else:
                instructions_to_do.append(instruction)
        elif "LSHIFT" in instruction:
            operands = instruction.split(" -> ")[0]
            input_operands = operands.split(" LSHIFT ")
            output_operand = instruction.split(" -> ")[1]
            if input_operands[0] in wires:
                wires[output_operand] = wires[input_operands[0]] << int(input_operands[1])
            else:
                instructions_to_do.append(instruction)
        elif "RSHIFT" in instruction:
            operands = instruction.split(" -> ")[0]
            input_operands = operands.split(" RSHIFT ")
            output_operand = instruction.split(" -> ")[1]
            if input_operands[0] in wires:
                wires[output_operand] = wires[input_operands[0]] >> int(input_operands[1])
            else:
                instructions_to_do.append(instruction)
        elif "NOT" in instruction:
            operands = instruction.split(" -> ")[0]
            input_operands = operands.split("NOT ")
            output_operand = instruction.split(" -> ")[1]
            if input_operands[1] in wires:
                wires[output_operand] = 65535 - wires[input_operands[1]]
            else:
                instructions_to_do.append(instruction)
        else:
            print("unknown operation: {}".format(instruction))


print(wires)
print("TASK 1 - ")

print("TASK 2 - ")
