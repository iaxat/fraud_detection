graph = {'A': ['B', 'D', 'E'], 'B': ['C'], 'C': ['D', 'E'], 'D': ['C', 'E'], 'E': ['B']}

source = 'B'
path = []
stack = [source]
count = 0


while(len(stack) != 0):
    p = source
    s = stack.pop()
    if s not in path:
        path.append(s)
    if s not in graph:
        #leaf node
        continue
    for neighbor in graph[s]:
        if neighbor != source:
            stack.append(neighbor)
        else:
            path.append(p)
            continue

print(path)
# return " ".join(path)