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

print(solve_part_one("day8.txt"))