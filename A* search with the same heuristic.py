import heapq

def astar(start, goal, heuristic):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while frontier:
        _, current = heapq.heappop(frontier)
        
        if current == goal:
            break
            
        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current
    
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

graph = {
    'Start': ['A', 'B', 'C'],
    'A': ['C'],
    'B': ['D'],
    'D': ['D', 'G'],
    'C': ['C', 'G'],
    'G': []
}
start = 'Start'
goal = 'G'
heuristic = {
    'Start': 5,
    'A': 2,
    'B': 5,
    'D': 1,
    'C': 2,
    'G': 0
}
path = astar(start, goal, heuristic)
print("Path:", path)
