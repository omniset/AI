class Graph:
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict

    # BFS function
    def BFS(self, start, goal):
        # Create a queue for BFS and a dictionary to store visited vertices and their parent vertices
        queue = [(start, [start])]
        visited = {start: None}
        states_expanded = [start]

        while queue:
            # Dequeue a vertex and its path
            (vertex, path) = queue.pop(0)

            # If the vertex is the goal, return its path
            if vertex == goal:
                return (path, states_expanded)

            # Enqueue all the adjacent vertices of the dequeued vertex if they haven't been visited yet
            for neighbor in self.graph_dict[vertex]:
                if neighbor not in visited:
                    visited[neighbor] = vertex
                    queue.append((neighbor, path + [neighbor]))
                    states_expanded.append(neighbor)

        # If there is no path from start to goal, return None
        return (None, states_expanded)

# Define the graph
graph_dict = {
    'start': ['A', 'B', 'D'],
    'A': ['C'],
    'B': ['D'],
    'D': ['C', 'G'],
    'C': ['D', 'G']
}

graph = Graph(graph_dict)
start = 'start'
goal = 'G'
path, states_expanded = graph.BFS(start, goal)

# Print the path and states expanded
if path:
    print(f"Path from {start} to {goal}: {'-'.join(path)}")
else:
    print(f"No path from {start} to {goal}")

print(f"States expanded: {', '.join(states_expanded)}")
