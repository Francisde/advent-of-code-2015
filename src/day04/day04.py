import hashlib


file1 = open('puzzle04.txt', 'r')
Lines = file1.readlines()

count = 0
secret = ""
lowest_Fitting_number = 1
for line in Lines:

    print("Line {}: {}".format(count, line.strip()))
    secret = line.strip()
    count += 1

while lowest_Fitting_number < 100000000:
    test_string = secret + str(lowest_Fitting_number)
    test_hash = hashlib.md5(test_string.encode('utf-8')).hexdigest()
    if test_hash.startswith("000000"):
        break

    lowest_Fitting_number += 1

print("TASK 1 and 2 - lowest Fitting number: {}".format(lowest_Fitting_number))


