def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

params_map = {'x':0, 'm':1, 'a':2, 's':3}

def evaluate_item(workflows, item, current_workflow):
    if current_workflow == 'A':
        return True
    
    if current_workflow == 'R':
        return False
    
    for condition in workflows[current_workflow]:
        if '>' in condition:
            param, value = condition.split('>')
            check, other_workflow = value.split(':')
            if item[params_map[param]] > int(check):
                return evaluate_item(workflows, item, other_workflow)
        elif '<' in condition:
            param, value = condition.split('<')
            check, other_workflow = value.split(':')
            if item[params_map[param]] < int(check):
                return evaluate_item(workflows, item, other_workflow)
        else:
            return evaluate_item(workflows, item, condition)
    pass

def solve_part_one(filename):
    workflows = {}
    items = []
    accepted = []
    rejected = []
    data = parse_input(filename)
    
    # Parse workflows
    while(data[0] != ''):
        name, rules = data[0].split('{')
        workflows[name] = rules.strip('{}').split(",")
        data = data[1:]
    
    data = data[1:]

    # Parse items
    while(data != []):
        x, m, a, s = data[0].strip('{}').split(',')
        x = x.split('=')[-1]
        m = m.split('=')[-1]
        a = a.split('=')[-1]
        s = s.split('=')[-1]
        items.append((int(x), int(m), int(a), int(s)))
        data = data[1:]

    for item in items:
        if evaluate_item(workflows, item, 'in'):
            accepted.append(item)
        else:
            rejected.append(item)

    total = 0
    for item in accepted:
        total += sum([item[0], item[1], item[2], item[3]])
    
    return total

def solve_part_two(filename):
    # TODO: Construct a graph from the 'accepted' state working backwards, 
    # accumulating conditions that MUST be met for items to be accepted.
    return 0

print(solve_part_one("day19.txt"))
print(solve_part_two("day19.txt"))

