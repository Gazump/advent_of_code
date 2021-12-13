# NMB
# Advent of Code 2021
# Problem 12b

def count_paths(graph, node, seen, twice):
    if node == 'end':
        return 1
    count = 0
    for adj in graph[node]:
        if adj != 'start':
            if adj[0].isupper() or adj not in seen:
                count += count_paths(graph, adj, seen + [adj], twice)
            elif not twice:
                count += count_paths(graph, adj, seen, True)
    return count

lines = open('input_12.txt','r').read().splitlines()

graph = {}
for line in lines:
    tokens = line.split('-')    
    if tokens[0] not in graph:
        graph[tokens[0]] = set()
    if tokens[1] not in graph:
        graph[tokens[1]] = set()
    graph[tokens[0]].add(tokens[1])
    graph[tokens[1]].add(tokens[0])

print(count_paths(graph, 'start', ['start'], False))


        



        


