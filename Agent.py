from random import randint
class Agent:
	
	def __init__(self,start,maze):
		self.start = start
		self.maze = maze
		self.current_pos = start
		self.current_node = self.maze.maze[start]
		
	def simple_discovery(self):
		#loop until all nodes have been discovered
		while len(self.maze.undiscovered) > 0:
			#retrieve the next node
			next = self.discover(self.current_node)
			next_pos = next.get_pos()
			#find path to node
			path = self.find_path(self.current_pos,next_pos)
			#move along path and update the current node
			self.move(path)
			self.current_node = next
			
	#simple discovery scheme
	#Takes in a node and returns a node
	def discover(self,position):
		#node that you are on is now discovered
		position.set_discovered()
		self.maze.undiscovered.remove(position)
		
		#create dict of nodes that are adjacent 
		keys = position.get_edges().keys()
		values = position.get_edges().values()
		neighbors = {}
		for i in range(len(keys)):
			if self.maze.maze[keys[i]].get_discovered() == False:
				temp_dict = {keys[i]:values[i]}
				neighbors.update(temp_dict)
		
		#if there is nothing left just return the position
		if len(self.maze.undiscovered) == 0:
			return position
			
		#if we are in a corner pick the next undiscovered node
		if len(neighbors.keys()) == 0:
			return self.maze.undiscovered[0]
			
		#otherwise determine what node to pick next
		#Once we have a more complex discovery scheme we will have a more
		#deterministic way of picking which neighbor will be moved to next
		else:
			#find the min edge weight and throw all edges into a list
			min_dist = min(neighbors.values())
			matched = [k for k in neighbors if neighbors[k] == min_dist]
			if len(matched) > 1:
				return self.maze.maze[matched[randint(0,len(matched)-1)]]
			else:
				return self.maze.maze[matched[0]]
	
	#very simple pathfinding scheme
	#Takes in Coordinates and returns a path of coordinates
	def find_path(self,a,b,path=[]):
		#simply append to the path until the end it found
		path = path + [a]
		if a == b:
			return path
			
		if not self.maze.maze.has_key(a):
			return None
		
		#after all paths are found determine the shortest by
		#the len() of the path since edge weights are 1
		shortest = None
		for pos in self.maze.edges[a]:
			if pos not in path:
				new_path = self.find_path(pos,b,path)
				if new_path:
					if not shortest or len(new_path) < len(shortest):
						shortest = new_path
		return shortest
		
	#takes a list of coordinates and moves the agent along them
	def move(self,path):
		for pos in path:
			print "Moving to position:" + str(pos) + "\n"
			self.current_pos = pos