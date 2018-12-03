from Node import Node

FILE_NAME = "maze.txt"

class Maze:
  
  def __init__(self, filename):
    self.gg = self.read_file(filename) ##read file
    self.grid = self.gg[0]
    self.graph = self.gg[1]
    self.nodes = []
    self.process_valid_nodes()
    self.generate_edges()
    self.maze = {node.get_pos():node for node in self.nodes}
    self.edges = {node.get_pos():node.get_edges() for node in self.nodes}
    self.undiscovered = [node for node in self.nodes if node.get_discovered() == False]

  def generate_edges(self):
    for node in self.nodes:
      node.make_edges()

  def remove_discovered_node(self,node):
    self.undiscovered.remove(node)


  def read_file(self, filename):
    filename = FILE_NAME ##TEMPERTORARY
    grid = []
    graph = []
    row = -1
    with open(filename) as f:
      for line in f:
        grid.append([])
        graph.append([])
        row += 1
        col = -1
        i = 0
        for c in line:
          if c == '\n':
            continue
          if i % 4 == 0:
            col += 1
            grid[row].append([])
            posTuple = (col, row)
            graph[row][col] = Node(None, None, None, None, posTuple, None)
            grid[row][col] = [0]*4
          grid[row][col][i % 4] = c
          i += 1
    return [grid, graph]


  def make_connections(self):
    for y in range(len(self.grid)):
      for x in range(len(self.grid[y])):

        if self.grid[y][x][1] == 0 and y + 1 < len(self.grid) and self.grid[y + 1][x][0] == 0:
          self.graph[y][x].down = self.graph[y + 1][x]
          self.graph[y + 1][x].top = self.graph[y][x]
        
        if self.grid[y][x][3] == 0 and x + 1 < len(self.grid[y]) and self.grid[y][x + 1][2] == 0:
          self.graph[y][x].right = self.graph[y][x + 1]
          self.graph[y][x + 1].left = self.graph[y][x]


  def BFS(self, node):
    node.setValid(True)
    self.nodes.append(node)
    
    if(node.down != None and node.down.valid == False):
      self.BFS(node.down)
    if(node.right != None and node.right.valid == False):
      self.BFS(node.right)  
    if(node.up != None and node.up.valid == False):
      self.BFS(node.up)
    if(node.left != None and node.left.valid == False):
      self.BFS(node.left) 

  
  def process_valid_nodes(self):
    node = self.graph[0][0]
    self.BFS(node) 