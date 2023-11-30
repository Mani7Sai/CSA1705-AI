import matplotlib.pyplot as plt
import networkx as nx
from itertools import permutations

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance + graph[path[-1]][path[0]]

def travelling_salesman_bruteforce(graph):
    num_cities = graph.num_vertices
    cities = list(range(num_cities))

    # Generate all possible permutations of cities
    all_permutations = permutations(cities)

    min_distance = float('inf')
    best_path = None

    for path in all_permutations:
        distance = calculate_total_distance(path, graph.graph)
        if distance < min_distance:
            min_distance = distance
            best_path = path

    return best_path, min_distance

def draw_graph(graph, path):
    G = nx.Graph()

    for i in range(graph.num_vertices):
        G.add_node(i)

    for i in range(graph.num_vertices):
        for j in range(i + 1, graph.num_vertices):
            G.add_edge(i, j, weight=graph.graph[i][j])

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')

    # Highlight the TSP path
    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    edges.append((path[-1], path[0]))
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)

    plt.show()

if __name__ == "__main__":
    # Get the number of cities from the user
    num_cities = int(input("Enter the number of cities: "))

    # Create a graph with the given number of cities
    tsp_graph = Graph(num_cities)

    # Get distances between cities from the user
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            weight = int(input(f"Enter distance from city {i + 1} to city {j + 1}: "))
            tsp_graph.add_edge(i, j, weight)

    best_path, min_distance = travelling_salesman_bruteforce(tsp_graph)

    print("Best Path:", best_path)
    print("Minimum Distance:", min_distance)

    draw_graph(tsp_graph, best_path)
