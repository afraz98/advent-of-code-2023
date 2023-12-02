
def solve_part_one(filename):
    return sum(list(map(lambda x : (10*x[0]) + x[-1], list(map(lambda x : [int(i) for i in list(x) if i.isdigit()], [line.strip('\r\n') for line in open(filename, 'r')])))))

print(solve_part_one('day1.txt'))