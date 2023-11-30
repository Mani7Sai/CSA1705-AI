from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)

        while queue:
            current_node = queue.popleft()
            print(current_node)

            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

if __name__ == "__main__":
    graph = Graph()

    while True:
        node = input("Enter a node (or 'done' to finish): ").upper()
        if node == 'DONE':
            break

        neighbors = input(f"Enter neighbors for node {node} separated by spaces: ").split()
        graph.add_edge(node, neighbors)
    start_node = input("Enter the starting node for BFS traversal: ").upper()

    if start_node in graph.graph:
        print("BFS Traversal:")
        graph.bfs(start_node)
    else:
        print(f"Node {start_node} not found in the graph.")
