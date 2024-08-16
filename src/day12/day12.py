import json

file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

def get_sum_depth_search(input_json):
    # perform dict action
    sum = 0
    if isinstance(input_json, dict):
        all_keys = list(input_json.keys())
        for key in all_keys:
            if isinstance(input_json[key], dict) or isinstance(input_json[key], list):
                sum += get_sum_depth_search(input_json[key])
                pass
            else:
                if isinstance(input_json[key], int):
                    sum += input_json[key]
    elif isinstance(input_json, list):

        # should be an array
        for entry in input_json:
            if isinstance(entry, dict) or isinstance(entry, list):
                sum += get_sum_depth_search(entry)
                pass
            else:
                if isinstance(entry, int):
                    sum += entry
    else:
        print("something strange happened")
    return sum

def get_sum_depth_search_part2(input_json):
    print(input_json)
    # perform dict action
    sum = 0
    if isinstance(input_json, dict):
        all_keys = list(input_json.keys())
        if "red" in all_keys:
            return 0
        for key in all_keys:
            if isinstance(input_json[key], dict) or isinstance(input_json[key], list):
                sum += get_sum_depth_search_part2(input_json[key])
                pass
            else:
                print(input_json[key])
                if input_json[key] == 'red':
                    return 0
                elif isinstance(input_json[key], int):
                    sum += input_json[key]
    elif isinstance(input_json, list):

        # should be an array
        for entry in input_json:
            if isinstance(entry, dict) or isinstance(entry, list):
                sum += get_sum_depth_search_part2(entry)
                pass
            else:
                if isinstance(entry, int):
                    sum += entry
    else:
        print("something strange happened")
    return sum

count = 0
json_input_string = ""
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    json_input_string = input_line

parsed_json_input = json.loads(json_input_string)
print(parsed_json_input)

sum = get_sum_depth_search(parsed_json_input)
sum2 = get_sum_depth_search_part2(parsed_json_input)

print("TASK 1 - Sum of all numbers: {}".format(sum))

print("TASK 2 - Sum of all numbers: {}".format(sum2))