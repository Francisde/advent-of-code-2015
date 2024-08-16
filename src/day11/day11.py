
file1 = open('puzzle11.txt', 'r')
Lines = file1.readlines()

def increase_password(seq):
    new_password = seq
    i = 7
    while i >= 0:
        if new_password[i] == 'z':
            new_password = new_password[0:i]  + 'a' + new_password[i+1:]
            i -= 1
        else:
            char_ = ord(new_password[i])
            char_ += 1
            new_password = new_password[0:i]  + chr(char_) + new_password[i+1:]
            break
    return new_password

def check_passwort_requirements(password):
    # contains one 3 letter increasing step?
    increasing_step = False
    for i in range(len(password) - 2):
        char_1 = ord(password[i])
        char_2 = ord(password[i + 1])
        char_3 = ord(password[i + 2])
        if char_2 == char_1 + 1 and char_3 == char_2 + 1:
            increasing_step = True
            break
    if not increasing_step:

        return False
    # contains no forbidden letters
    no_forbidden_letter = True
    if 'i' in password or 'o' in password or 'l' in password:
        no_forbidden_letter = False
    if not no_forbidden_letter:

        return False
    # contains two pairs
    contains_pairs = False
    for i in range(len(password) -1):
        if password[i] == password [i + 1]:
            j = i + 2
            while j < len(password) - 1:
                if password[j] == password[j + 1] and password[j] != password[i]:
                    contains_pairs = True
                    break
                j += 1
            if contains_pairs:
                break


    return contains_pairs


count = 0
old_password = ""
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    old_password = input_line


new_password = old_password
while(True):
    new_password = increase_password(new_password)
    if check_passwort_requirements(new_password):

        break
print("TASK 1 - New Password: {}".format(new_password))

print("TASK 2 - ")