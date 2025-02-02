# Brandon Cazares
# CECS 427 Sec 1
# Professor Morales Ponce
# Graphs Assignment #1
# Due Date: 2/6/2025
import networkx as nx
import matplotlib.pyplot as plt
import json

# We're going to implement our GraphManager class
class GraphManager:
    def __init__(self):
        self.graph = nx.DiGraph()

    # we're going to add our edges to our graph
    def add_edges(self, edges):
            """Add edges to the graph"""
            for edge in edges:
                if len(edge) == 3:
                    u, v, weight = edge
                    self.graph.add_edge(u, v, weight=weight)
                else:
                    self.graph.add_edge(*edge)
    # next, we're going to save our graphs to our file.
    def save_to_file(self, filename):
            """Save the graph to a file in JSON format."""
            data = nx.node_link_data(self.graph)
            with open(filename, 'w') as file:
                json.dump(data, file)
    # after this, we're going to load our data from the file.
    def load_from_file(self, filename):
            """Load a graph from a file"""
            with open(filename, 'r') as file:
                data = json.load(file)
                self.graph = nx.node_link_graph(data)

    # we'll compute our shortest paths from a speciifed source node.
    def compute_shortest_paths(self, source):
        """Compute shortest paths from a specified source node."""
        try:
            return nx.single_source_dijkstra_path(self.graph, source)
        except nx.NetworkXNoPath:
            print(f"No paths found from source node {source}.")
            return {}
    # we'll visualize the graph with optional shortest paths when highlighted.
    def visualize(self, shortest_paths=None):
        """Visualize the graph with optional shortest paths highlighted."""
        pos = nx.spring_layout(self.graph)

        # Draw the graph
        nx.draw(self.graph, pos, with_labels=True, node_color='darkblue', edge_color='gray', node_size=500, font_size=10)

        if shortest_paths:
            # Highlight shortest paths
            for path in shortest_paths.values():
                # our edges are highlighted as a path and then zipped
                edges = list(zip(path, path[1:]))
                nx.draw_networkx_edges(
                    self.graph, pos, edgelist=edges, edge_color='red', width=2
                )

        plt.show()
# Example Usage
def main():
    gm = GraphManager()

    # Add edges
    edges = [("A", "B", 2), ("A", "C", 5), ("B", "C", 1), ("C", "D", 3)]
    gm.add_edges(edges)

    # Save to file
    gm.save_to_file("graph.json")

    # Load from file
    gm.load_from_file("graph.json")

    # Compute shortest paths from a source node
    source_node = "A"
    shortest_paths = gm.compute_shortest_paths(source_node)
    print(f"Shortest paths from {source_node}: {shortest_paths}")

    # Visualize the graph and shortest paths
    gm.visualize(shortest_paths)

if __name__ == "__main__":
    main()