from shutil import which

file1 = open('puzzle02.txt', 'r')
Lines = file1.readlines()

count = 0
floor_count = 0
character_sent_santa_to_basement = 1
required_wrapping_paper = 0
ribbon_length = 0
for line in Lines:
    print("Line {}: {}".format(count, line.strip()))
    dimensions = line.strip().split("x")
    print(dimensions)
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    int_dimensions = [l, w, h]
    int_dimensions.sort()
    ribbon_length += (w * l * h)
    ribbon_length += (int_dimensions[0] + int_dimensions[0] + int_dimensions[1] + int_dimensions[1])
    surface = 2*l*w + 2*w*h + 2*h*l
    lw = l * w
    lh = l * h
    wh = w * h
    slack = min(lw, lh, wh)
    print("surface = {} + slack: {}".format(surface, slack))
    required_wrapping_paper += (surface + slack)
    count += 1


print("TASK 1 - required square feet of wrapping paper: {}".format(required_wrapping_paper))
print("TASK 2 - required ribbon length: {} feet".format(ribbon_length))