from collections import deque
def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return explore_shortest_path(graph, node_A, node_B)
    
def explore_shortest_path(graph, src, dst):
    queue = deque([(src, 0)])
    visited = set([src])

    while queue:
        current, distance = queue.popleft()

        if current == dst:
            return distance 
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return -1

    
    
   
   
    

def build_graph(edges):
    graph = {}
    for edge in edges:
        a , b = edge
        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph












edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z') )# -> 2