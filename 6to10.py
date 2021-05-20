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

path = recursive_dfs(graph, "C")
print(" ".join(path))


# 6. 