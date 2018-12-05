class Maze:
    def __init__(self, nodes):
        self.nodes = nodes
        self.generate_edges()
        self.maze = {node.get_pos(): node for node in nodes}
        self.generate_edges()
        self.edges = {node.get_pos(): node.get_edges() for node in nodes}
        self.undiscovered = [node for node in nodes if node.get_discovered() == False]

    def generate_edges(self):
        for node in self.nodes:
            node.make_edges()

    def remove_discovered_node(self, node):
        self.undiscovered.remove(node)