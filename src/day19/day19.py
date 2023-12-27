from visualize import visualize_graph
from itertools import product

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

def traverse_graph(workflows):
    graph = {'in':{'x':[(0, 4000)], 'm':[(0, 4000)], 'a':[(0, 4000)], 's':[(0,4000)]}}
    nodes = ['in']

    while nodes != []:
        node = nodes.pop(0)

        if node not in graph.keys():
            graph[node] = {}

        if node not in graph.keys():
            graph[node] = {'x':[], 'm':[], 'a':[], 's':[]}

        for connection in workflows[node]:
            if '>' in connection:
                condition, next_node = connection.split(":")
                param, value = condition.split(">")
                
                if next_node not in graph.keys():
                    graph[next_node] = {'x':[], 'm':[], 'a':[], 's':[]}


                # Add processed range(s) to next node's graph
                for index in range(len(graph[node][param])):
                    if int(value) > graph[node][param][index][0]:
                        graph[next_node][param].append((int(value), graph[node][param][index][1]))
                        graph[node][param][index] = (graph[node][param][index][0], int(value))

                # Add unprocessed ranges
                for param in ['x', 'm', 'a', 's']:
                    if graph[next_node][param] == []:
                        graph[next_node][param] = graph[node][param]
                
                nodes.append(next_node)
                
            elif '<' in connection:
                condition, next_node = connection.split(":")
                param, value = condition.split("<")

                if next_node not in graph.keys():
                    graph[next_node] = {'x':[], 'm':[], 'a':[], 's':[]}

                # Add processed range(s) to next node's graph
                for index in range(len(graph[node][param])):
                    if int(value) < graph[node][param][index][1]:
                        graph[next_node][param].append((graph[node][param][index][0], int(value)))
                        graph[node][param][index] = (int(value), graph[node][param][index][1])
                

                # Add unprocessed ranges
                for param in ['x', 'm', 'a', 's']:
                    if graph[next_node][param] == []:
                        graph[next_node][param] = graph[node][param]
                
                nodes.append(next_node)
            else:
                if connection not in graph.keys():
                    graph[connection] = {'x':[], 'm':[], 'a':[], 's':[]}

                # Add unprocessed ranges
                for param in ['x', 'm', 'a', 's']:
                    if graph[connection][param] == []:
                        graph[connection][param] = graph[node][param]
                
                nodes.append(connection)
    return graph

def find_product(list):
    prod = 1
    for el in list:
        prod *= el
    return prod

def solve_part_two(filename):
    workflows = {}
    data = parse_input(filename)
    
    # Parse workflows
    while(data[0] != ''):
        name, rules = data[0].split('{')
        workflows[name] = rules.strip('{}').split(",")
        data = data[1:]

    workflows['A'] = []
    workflows['R'] = []
    graph = traverse_graph(workflows)

    completed_graph = {'A':{'x':[], 'm':[], 'a':[], 's':[]}}
    for key in graph['A'].keys():
        for r in graph['A'][key]:
            completed_graph['A'][key].append(abs(r[1]-r[0]))
    
    return sum([find_product(list) for list in list(product(completed_graph['A']['x'], completed_graph['A']['m'], completed_graph['A']['a'], completed_graph['A']['s']))])

print(solve_part_one("day19.txt"))
print(solve_part_two("day19_test.txt"))

