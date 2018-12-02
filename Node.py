from collections import defaultdict
class Node:

	def __init__(self,up,down,left,right,pos,discovered):
		self.up = up #node above, below, left, and right
		self.down = down 
		self.left = left
		self.right = right
		self.pos = pos #tuple for the position
		self.discovered = discovered
		self.edges = {} #dict of edges, keys are coords and values are edge weight
		
		#setting up vars for D* Lite
		self.g = float('inf')
		self.rhs = float('inf')

	def __str__(self):
		return str(self.pos[0]) + str(self.pos[1])
		
	def set_up(self,node):
		self.up = node
		
	def set_down(self,node):
		self.down = node
		
	def set_left(self,node):
		self.left = node
		
	def set_right(self,node):
		self.right = node
		
	def set_discovered(self):
		self.discovered = True
		
	def get_pos(self):
		return self.pos
		
	def get_edges(self):
		return self.edges
		
	def get_discovered(self):
		return self.discovered
	
	def make_edges(self):
		connections = [self.up,self.down,self.right,self.left]
		weights = [1,1,1,1]
		for i in range(4):
			if connections[i]:
				self.edges[connections[i].get_pos()] = weights[i]