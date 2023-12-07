from functools import reduce

def find_methods_to_beat_record(races):
    methods_to_beat_record = []
    for race in races:
        methods = 0
        for time in range(int(race[0])):
            if(int(race[0]) - time) * (time) > int(race[1]):
                methods += 1
        methods_to_beat_record.append(methods)
    return reduce(lambda x, y: x * y, methods_to_beat_record)

def solve_part_one(filename):
    input = [line.strip('\r\n').split(" ")[1:] for line in open(filename, "r")]
    for line in input:
        line = filter(lambda x: x != '', [x for x in line])
    
    times = input[0]
    times = list(filter(lambda x: x!= '', times))
    
    distances = input[1]
    distances = list(filter(lambda x: x!='', distances))

    races = list(zip(times, distances))
    return find_methods_to_beat_record(races)

print(solve_part_one("day6.txt"))