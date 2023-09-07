def has_path(graph, src, dst):
    stack = [src]
    while len(stack) > 0:
        current = stack[-1]
        poped = stack.pop()
        if poped == dst:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False







graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'i', 'h'))