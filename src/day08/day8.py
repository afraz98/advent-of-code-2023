import math
def solve_part_one(filename):
    step = 0

    input = [line.strip("\n") for line in open(filename, "r") if line != "\n"]
    moves = input[0]

    input = input[1:]
    nodes = {}

    
    for line in input:
        node, options = line.split(" = ")
        nodes[node] = options.replace("(", "").replace(")", "").replace(" ","").split(",")
    
    src = "AAA"
    while src != "ZZZ":
        src = nodes[src][0 if moves[step % len(moves)] == 'L' else 1]
        step += 1
    
    return step

# Python 3.8.10 shenanigans :-)
def least_common_multiple(integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // math.gcd (a, b)
    return a

def solve_part_two(filename):
    step = 0

    input = [line.strip("\n") for line in open(filename, "r") if line != "\n"]
    moves = input[0]

    input = input[1:]
    nodes = {}

    
    for line in input:
        node, options = line.split(" = ")
        nodes[node] = options.replace("(", "").replace(")", "").replace(" ","").split(",")
    
    src_nodes = []
    for node in nodes.keys():
        if node[-1] == "A":
            src_nodes.append(node)

    steps = []
    for i in range(0, len(src_nodes)):
        step = 0
        src = src_nodes[i]
        while(src[-1] != "Z"):
            src = nodes[src][0 if moves[step % len(moves)] == 'L' else 1]
            step += 1
        steps.append(step)

    return least_common_multiple(steps)

print(solve_part_one("day8.txt"))
print(solve_part_two("day8.txt"))
