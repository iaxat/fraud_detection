def recursive_dfs(graph, source,path = []):

    if source not in path:
        path.append(source)
        if source not in graph:
            # leaf node, backtrack
            return path
        for neighbour in graph[source]:
            path = recursive_dfs(graph, neighbour, path)
    else:
        path.append(source)
    
    return path

graph = {'A': ['B', 'D', 'E'], 'B': ['C'], 'C': ['D', 'E'], 'D': ['C', 'E'], 'E': ['B']}


# 6. C to C
source = 'C'
path = recursive_dfs(graph, source)
path_edit = path
print(" ".join(path))
temp_arr = []
start = 0
end = len(path_edit)-1
ways = []
if 'C' in path_edit:
    while end > 0:
        if path_edit[end] != source:
            path_edit.pop()
            end -= 1
        if path_edit[end] == source:
            temp_arr.append(end)
            end -= 1

    temp_arr = temp_arr[::-1]
    print(temp_arr)
else:
    print('so solution')



# 7. Trips from A to C
source = 'A'
path = recursive_dfs(graph, source)
path_edit = path
print(" ".join(path))
temp_arr = []
start = 0
end = len(path_edit)-1
ways = []
if 'C' in path_edit:
    while end > 0:
        if path_edit[end] != source:
            path_edit.pop()
            end -= 1
        if path_edit[end] == source:
            temp_arr.append(end)
            end -= 1

    temp_arr = temp_arr[::-1]
    print(temp_arr)
else:
    print('so solution')


# 8. A to C shortest route
source = 'C'
path = recursive_dfs(graph, source)
path_edit = path
print(" ".join(path))
temp_arr = []
start = 0
end = len(path_edit)-1
ways = []
if 'C' in path_edit:
    while end > 0:
        if path_edit[end] != source:
            path_edit.pop()
            end -= 1
        if path_edit[end] == source:
            temp_arr.append(end)
            end -= 1

    temp_arr = temp_arr[::-1]
    print(temp_arr)
else:
    print('so solution')


# 9. B to B 
source = 'C'
path = recursive_dfs(graph, source)
path_edit = path
print(" ".join(path))
temp_arr = []
start = 0
end = len(path_edit)-1
ways = []
if 'C' in path_edit:
    while end > 0:
        if path_edit[end] != source:
            path_edit.pop()
            end -= 1
        if path_edit[end] == source:
            temp_arr.append(end)
            end -= 1

    temp_arr = temp_arr[::-1]
    print(temp_arr)
else:
    print('so solution')


# 10. C to C trips with distance less than 30
source = 'C'
path = recursive_dfs(graph, source)
path_edit = path
print(" ".join(path))
temp_arr = []
start = 0
end = len(path_edit)-1
ways = []
if 'C' in path_edit:
    while end > 0:
        if path_edit[end] != source:
            path_edit.pop()
            end -= 1
        if path_edit[end] == source:
            temp_arr.append(end)
            end -= 1

    temp_arr = temp_arr[::-1]
    print(temp_arr)
else:
    print('so solution')