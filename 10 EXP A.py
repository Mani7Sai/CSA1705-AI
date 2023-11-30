import matplotlib.pyplot as plt
import networkx as nx
import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.neighbors = {}

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, node1, node2, cost):
        self.nodes[node1].add_neighbor(node2, cost)
        self.nodes[node2].add_neighbor(node1, cost)

def a_star(graph, start, goal):
    open_set = []
    closed_set = set()

    start_node = graph.nodes[start]
    goal_node = graph.nodes[goal]

    heapq.heappush(open_set, (start_node.heuristic, start_node, []))

    while open_set:
        _, current_node, path = heapq.heappop(open_set)

        if current_node.name == goal:
            return path + [goal]

        closed_set.add(current_node.name)

        for neighbor, cost in current_node.neighbors.items():
            if neighbor not in closed_set:
                neighbor_node = graph.nodes[neighbor]
                heuristic = neighbor_node.heuristic
                new_path = path + [current_node.name]
                heapq.heappush(open_set, (cost + heuristic, neighbor_node, new_path))

    return None

def draw_graph(graph, path):
    G = nx.Graph()

    for node_name, node in graph.nodes.items():
        G.add_node(node_name, heuristic=node.heuristic)

    for node_name, node in graph.nodes.items():
        for neighbor, cost in node.neighbors.items():
            G.add_edge(node_name, neighbor, weight=cost)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700)

    # Highlight the A* path
    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)

    nx.draw_networkx_edge_labels(G, pos, edge_labels={(path[i], path[i + 1]): graph.nodes[path[i]].neighbors[path[i + 1]] for i in range(len(path) - 1)}, font_color='b')

    plt.show()

if __name__ == "__main__":
    # Create a sample graph
    sample_graph = Graph()

    num_nodes = int(input("Enter the number of nodes: "))
    for _ in range(num_nodes):
        node_name = input("Enter node name: ")
        heuristic = float(input("Enter heuristic value for {}: ".format(node_name)))
        node = Node(node_name, heuristic)
        sample_graph.add_node(node)

    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        node1 = input("Enter the first node of the edge: ")
        node2 = input("Enter the second node of the edge: ")
        cost = float(input("Enter the cost of the edge between {} and {}: ".format(node1, node2)))
        sample_graph.add_edge(node1, node2, cost)

    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")

    if start_node not in sample_graph.nodes or goal_node not in sample_graph.nodes:
        print("Invalid start or goal node.")
    else:
        path = a_star(sample_graph, start_node, goal_node)

        if path:
            print("A* Path:", path)
            draw_graph(sample_graph, path)
        else:
            print("No path found.")
