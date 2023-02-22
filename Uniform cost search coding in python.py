import heapq

# Define the graph as a dictionary of dictionaries
graph = {
    'Start': {'A': 1, 'B': 5, 'D': 3},
    'A': {'C': 3},
    'B': {'D': 2},
    'D': {'C': 1, 'Goal': 7},
    'C': {'Goal': 2}
}

# Uniform Cost Search function
def ucs(graph, start, goal):
    # Create a priority queue for UCS and a dictionary to store visited vertices and their parent vertices
    pq = []
    heapq.heappush(pq, (0, start))
    visited = {start: None}
    states_expanded = [start]

    while pq:
        # Pop the vertex with the smallest cost so far from the priority queue
        (cost, vertex) = heapq.heappop(pq)

        # If the vertex is the goal, trace its path and return it
        if vertex == goal:
            path = []
            while vertex:
                path.insert(0, vertex)
                vertex = visited[vertex]
            return (path, states_expanded)

        # Push all the adjacent vertices of the popped vertex into the priority queue if they haven't been visited yet
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited[neighbor] = vertex
                new_cost = cost + graph[vertex][neighbor]
                heapq.heappush(pq, (new_cost, neighbor))
                states_expanded.append(neighbor)

    return (None, states_expanded)

# Call the UCS function to find the path and states expanded
start = 'Start'
goal = 'Goal'
path, states_expanded = ucs(graph, start, goal)

print("Path Returned:", ', '.join(path))
