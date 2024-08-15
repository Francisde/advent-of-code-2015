
file1 = open('puzzle08.txt', 'r')
Lines = file1.readlines()
hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
count = 0
code_chars = 0
in_memory_chars = 0
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))

    count += 1
    current_code_chars = len(input_line)
    code_chars += current_code_chars
    current_memory_chars = current_code_chars - 2
    old_input_line = input_line
    input_line = input_line[1:len(input_line)-1]

    # escape "
    escapes = input_line.count('\\"')
    current_memory_chars -= escapes
    escapes_anf = escapes
    escapes = input_line.count('\\\\')
    current_memory_chars -= escapes
    escapes_back = escapes
    # check for ascii escapes

    escapes = 0
    for i in range((len(input_line) - 1)):
        if input_line[i:i+2] == "\\x":

            if input_line[i+2] in hex_chars and input_line[i+3] in hex_chars:
                escapes += 1

    current_memory_chars -= (escapes * 3)
    in_memory_chars += current_memory_chars
    if len(eval(old_input_line)) != current_memory_chars:

        print("sequence: {}, code-chars: {}, memory-chars: {}, diff: {}".format(input_line,current_code_chars, current_memory_chars, current_code_chars - current_memory_chars ))
        print(len(eval(input_line)))
        print("escapes anf: {}, escapes back: {}, escapes hex: {}".format(escapes_anf, escapes_back, escapes))

print(code_chars)
print(in_memory_chars)

print(len("jctcqra\"\x05dhlydpqamorqjsijt\\xjdgt"))
print("TASK 1 - needed sum = {}".format(code_chars - in_memory_chars))


# task 2
print("starting task 2")
code_chars = 0
encoded_code_chars = 0
for line in Lines:
    input_line= line.strip()
    # print("Line {}: {}".format(count, input_line))
    current_code_chars = len(input_line)
    number_of_quotes = input_line.count("\"")
    number_of_backslashs = input_line.count("\\")
    current_encoded_code_chars = current_code_chars + number_of_quotes + number_of_backslashs + 2
    print("seq: {}, modified: , old chars: {}, new chars: {}".format(input_line, current_code_chars, current_encoded_code_chars))
    code_chars += current_code_chars
    encoded_code_chars += current_encoded_code_chars

print("TASK 2 - sum = {}".format(encoded_code_chars - code_chars))
