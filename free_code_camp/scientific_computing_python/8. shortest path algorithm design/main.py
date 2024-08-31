"""
copper = {
    'species': 'Guinea Pig',
    'age': 2      
          }

print(copper['species'])

# add a new key/value pair:
copper['food'] = 'hay'
print(copper)

# reassign a value:
copper['species'] = 'Cavia porcellus'
print(copper)

# itterate over the KEYS in a dict:
for i in copper:
    print(i)

# itterate over the VALUES in a dict:
for i in copper.values():
    print(i)

# itterate over the KEYS/VALUE PAIRS in a dict (stored in tuples):
for i in copper.items():
    print(i)

# And to print the key value pairs as strings:
for i, j in copper.items():
    print(i, j)

# Remove a key/value pair:
del copper['age']

"""

# A graph is called a weighted graph when its edges are associated with weights, representing a distance, time or other quantitative value.
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# The algorithm will start at a specified node. Then it will explore the graph to find the shortest path between the starting node, or source, and all the other nodes.

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A', 'F')