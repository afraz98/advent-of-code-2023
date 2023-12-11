def find_sum(lines):
    return sum(list(map(lambda x : (10*x[0]) + x[-1], list(map(lambda x : [int(i) for i in list(x) if i.isdigit()], lines)))))

def solve_part_one(filename):
    return find_sum([line.strip('\r\n') for line in open(filename, 'r')])

def solve_part_two(filename):
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    
    lines = [line.strip('\r\n') for line in open(filename, 'r')]
    parsed_lines = []
    sum = 0
    for line in lines:
        first_indices = []
        last_indices = []
        for number in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if number in line:
                first_indices.append((number, line.index(number))) # <value, position>
                last_indices.append((number, line.rindex(number)))
        first_indices.sort(key=lambda x: x[1])
        last_indices.sort(key=lambda x: x[1])

        first_number = first_indices[0]
        last_number = last_indices[-1]

        parsed_lines.append((first_number, last_number))
        sum += (10*number_dict[first_number[0]]) + number_dict[last_number[0]]
    return sum

# Work in progress
def solve_part_two_optimized(filename):
    lines = [line.strip('\r\n') for line in open(filename, 'r')]
    parsed_lines = []

    number_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    sum = 0
    for line in lines:
        print(line)
        temp = line
        for number in number_list:
            temp = temp.replace(number, str(number_list.index(number)))
        values = [int(i) for i in temp if i.isdigit()]
        sum += (10*values[0]) + values[-1]
        print(temp + "->", values[0], values[-1], sum)
    return sum
    



# print(solve_part_one('day1.txt'))
# print(solve_part_two('day1.txt'))
print(solve_part_two_optimized('day1_test.txt'))