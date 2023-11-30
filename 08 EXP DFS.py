# DFS algorithm implementation in Python with user input

# Define the DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)

# Take user input to build the graph
graph = {}
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    node1, node2 = input("Enter edge (node1 node2): ").split()
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)
    graph[node2].append(node1)

# Take user input for the starting node
start_node = input("Enter the starting node: ")

# Call the DFS function with the user-defined graph and starting node
dfs(graph, start_node)
