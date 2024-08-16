
file1 = open('puzzle14.txt', 'r')
Lines = file1.readlines()

def get_distance_for_reindeer(reindeer, seconds):
    counter = 0
    km = 0
    run_phase = True
    phase_counter = 0
    while counter < seconds:
        counter += 1
        if run_phase:
            km += speed[reindeer]
            phase_counter += 1
            if phase_counter == duration[reindeer]:
                run_phase = False
                phase_counter = 0
        else:
            phase_counter += 1
            if phase_counter == rest[reindeer]:
                run_phase = True
                phase_counter = 0
    return km

def get_points_for_reindeers(reindeers_list, seconds):
    points = {}
    current_distance = {}
    phase_counter ={}
    run_phase ={}
    for reindeer in reindeers_list:
        current_distance[reindeer] = 0
        run_phase[reindeer] = True
        points[reindeer] = 0
        phase_counter[reindeer] = 0
    counter = 0
    while counter < seconds:
        counter += 1
        for reindeer in reindeers_list:
            if run_phase[reindeer]:
                current_distance[reindeer] += speed[reindeer]
                phase_counter[reindeer] += 1
                if phase_counter[reindeer] == duration[reindeer]:
                    run_phase[reindeer] = False
                    phase_counter[reindeer] = 0
            else:
                phase_counter[reindeer] += 1
                if phase_counter[reindeer] == rest[reindeer]:
                    run_phase[reindeer] = True
                    phase_counter[reindeer] = 0

        # award points:
        max_distance = 0
        for reindeer in reindeers_list:
            max_distance = max(current_distance[reindeer], max_distance)
        for reindeer in reindeers_list:
            if current_distance[reindeer] == max_distance:
                points[reindeer] += 1
    return points




count = 0
reindeers = []
speed = {}
duration = {}
rest = {}
distance = {}

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    split_string = input_line.split(" ")
    reindeers.append(split_string[0])
    speed[split_string[0]] = int(split_string[3])
    duration[split_string[0]] = int(split_string[6])
    rest[split_string[0]] = int(split_string[13])

print(speed)
print(duration)
print(rest)

maxDistance = 0

for reindeer in reindeers:
    distance = get_distance_for_reindeer(reindeer, 2503)
    print("Reindeer: {}, distance: {}".format(reindeer, distance))
    maxDistance = max(maxDistance, distance)

print("TASK 1 - max distance {}".format(maxDistance))

points = get_points_for_reindeers(reindeers, 2503)
print(points)
print("TASK 2 - ")