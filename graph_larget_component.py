def largest_component(graph):
    visited = set()
    largest = 0

    for node in graph:
        size = explore(graph, node, visited)
        if size > largest:
            largest = size

    return largest



def explore(graph, current, visited):
    if current in visited:
        return False
    
    visited.add(current)

    count = 1
    for neighbor in graph[current]:
        count += explore(graph, neighbor, visited)


    return count






print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4