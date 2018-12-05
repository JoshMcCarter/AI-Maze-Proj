from Node import Node

class Maze:
  
  def __init__(self, filename):
    self.gg = self.read_file(filename) ##read file
    self.grid = self.gg[0]
    self.graph = self.gg[1]
    self.make_connections()
    self.nodes = []
    self.process_valid_nodes()
    self.generate_edges()
    self.maze = {node.get_pos():node for node in self.nodes}
    self.edges = {node.get_pos():node.get_edges() for node in self.nodes}
    self.undiscovered = [node for node in self.nodes if node.get_discovered() == False]
    self.debug = False

  def generate_edges(self):
    for node in self.nodes:
      node.make_edges()

  def remove_discovered_node(self,node):
    self.undiscovered.remove(node)


  def read_file(self, filename):
    file = filename ##TEMPERTORARY
    grid = []
    graph = []
    row = -1
    with open(file) as f:
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
            graph[row].append([])
            posTuple = (col, row)
            grid[row][col] = [0]*4
            graph[row][col] = Node(False, False, False, False, posTuple, False)
            
          grid[row][col][i % 4] = c
          i += 1
    return [grid, graph]


  def make_connections(self):
    if self.debug is True:
      print("in make connections")
    for y in range(len(self.grid)):
      for x in range(len(self.grid[y])):
        if (y + 1 <= len(self.grid)-1) and (self.grid[y][x][1] != 1) and (self.grid[y][x][1] == self.grid[y+1][x][0]):
          #print("foo")
          self.graph[y][x].set_down(self.graph[y + 1][x])
          self.graph[y + 1][x].set_up(self.graph[y][x])
        if (x + 1 < len(self.grid[y])) and (self.grid[y][x][3] != 1) and (self.grid[y][x][3] == self.grid[y][x+1][2]):
          #print("bar")
          self.graph[y][x].set_right(self.graph[y][x + 1])
          self.graph[y][x + 1].set_left(self.graph[y][x])


  def BFS(self, node):
    queue = []
    queue.append(node)
    while len(queue) > 0:
      #print("WE ARE IN BFS")
      node = queue.pop(0)
      self.nodes.append(node)
      if node.down and node.down.valid == False:
        #print("SHOULD BE SETTING DOWN CONNECTION")
        node.down.set_valid(True)
        queue.append(node.down)      
      if node.up and node.up.valid == False:
        #print("SHOULD BE SETTING UP CONNECTION")
        node.up.set_valid(True)
        queue.append(node.up)
      if node.right and node.right.valid == False:
        #print("SHOULD BE SETTING RIGHT CONNECTION")
        node.right.set_valid(True)
        queue.append(node.right)
      if node.left and node.left.valid == False:
        #print("SHOULD BE SETTING LEFT CONNECTION")
        node.left.set_valid(True)
        queue.append(node.left)

  def process_valid_nodes(self):
    node = self.graph[0][0]
    self.BFS(node) 