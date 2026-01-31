"""
Graph using edge list
"""


class GraphUsingEdgeList:
    """Graph using edge list"""

    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vertex):
        """Add vertex in graph

        Args:
            vertex (str): a value for vertext
        """

        # First check vertex is already available or not in the graph
        if not vertex in self.vertices:
            self.vertices.append(vertex)

            print("Vertex is added in the graph.")
        else:
            print("Vertex already exists.")

    def add_edge(self, source: str, destination: str, weight=1):
        """Add edge between vertices

        Args:
            source (str): source vertex
            destination (str): destination vertex
            weight (int, optional): weight for the edge. Defaults to 1.
        """

        # Check source and destination are already there in vertices
        if source in self.vertices and destination in self.vertices:
            edge = (source, destination, weight)
            self.edges.append(edge)
            print(
                f"Edge is added from source {source} "
                f"to destination: {destination} with weight: {weight}"
            )
        else:
            if not source in self.vertices:
                print(f"Provided source: {source} does not exist in vertices")
            elif not destination in self.vertices:
                print(f"Provided destination: {destination} does not exist in vertices")

    def display(self):
        """Show all the vertices and edges of the graph"""

        # Print vertices
        for i, vertex in enumerate(self.vertices):
            print(f"Index: {i} vertex: {vertex}")

        # Print edges
        for i, (source, destination, weight) in enumerate(self.edges):
            print(f"{source} --({weight})--> {destination}")


if __name__ == "__main__":
    print("Testing graph using edge list")

    graph = GraphUsingEdgeList()

    graph.add_vertex("a")
    graph.add_vertex("b")
    graph.add_vertex("c")

    graph.add_edge("a", "b")
    graph.add_edge("b", "c")
    graph.add_edge("a", "c")

    graph.display()
