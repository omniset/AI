graph = {
    'Start': ['A', 'B'],
    'A': ['C', 'Goal'],
    'B': ['D'],
    'C': ['Goal'],
    'D': []
}

def dfs(start, goal, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    if start == goal:
        return visited
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs(neighbor, goal, visited)
            if path is not None:
                return path
    return None

path = dfs('Start', 'Goal')
print(path)
