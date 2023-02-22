graph = {
    'Start': {'A': 6, 'B': 2, 'D': 1},
    'A': {'C': 1},
    'B': {'D': 3},
    'D': {'C': 3, 'G': 1},
    'C': {'G': 1},
    'G': {}
}

heuristic = {
    'A': 2,
    'B': 5,
    'C': 2,
    'D': 1,
    'G': 0
}

def greedy_search(graph, heuristic, start, goal):
    visited = []
    queue = [(start, 0)]
    while queue:
        current_node, current_cost = queue.pop(0)
        if current_node == goal:
            visited.append(current_node)
            return visited
        if current_node not in visited:
            visited.append(current_node)
            neighbors = graph[current_node]
            neighbors_sorted = sorted(neighbors.items(), key=lambda x: heuristic[x[0]])
            for neighbor, cost in neighbors_sorted:
                if neighbor not in visited:
                    queue.append((neighbor, current_cost + cost))
    return visited

path = greedy_search(graph, heuristic, 'Start', 'G')
print("States Expanded:", ', '.join(path))
print("Path Returned:", '-'.join(path))
