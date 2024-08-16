
file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

def look_and_say(input_sequence, num):
    current_sequence = input_sequence
    for i in range(num):
        new_sequence = ""
        current_char = ""
        char_counter = 0
        first_start = True
        for char in current_sequence:
            if char != current_char:
                if first_start:
                    first_start = False
                else:
                    new_sequence += "{}{}".format(char_counter, current_char)
                char_counter = 1
                current_char = char
            else:
                char_counter += 1
        new_sequence += "{}{}".format(char_counter, current_char)
        current_sequence = new_sequence

    return current_sequence


count = 0
start_sequence = ""
iterations = 40
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    start_sequence = input_line



result = look_and_say(start_sequence, iterations)
print("TASK 1 - string length: {}".format(len(result)))

iterations = 50
result = look_and_say(start_sequence, iterations)
print("TASK 2 - string length: {}".format(len(result)))