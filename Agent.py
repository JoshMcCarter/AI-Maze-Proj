import queue
from random import randint
class Agent:
	
	def __init__(self,start,maze):
		self.start = start
		self.maze = maze
		self.current_pos = start.pos
		self.current_node = start
		self.start.set_discovered()
		self.maze.undiscovered.remove(self.start)
		self.path = []
		self.goal = False
		self.undiscovered = queue.LifoQueue() #keep history of undiscovered nodes passed
		
	def move(self,path):
		#print path
		self.current_pos = path[0].pos
		self.current_node = path[0]
		#print self.current_node
		path.remove(self.current_node)
		
	def discover(self,current_node):
		#scan for undiscovered nodes adjacent to the current position
		undiscovered_neighbors = []
		for key1,key2 in current_node.edges:
			if self.maze.maze[(key1,key2)].get_discovered() == False:
				undiscovered_neighbors.append(self.maze.maze[(key1,key2)])
		
		#print undiscovered_neighbors
		#if there are undiscovered neighbors just pick one of them
		if len(undiscovered_neighbors) > 0:
			pick_neighbor = randint(0,len(undiscovered_neighbors)-1)
			next_node = undiscovered_neighbors[pick_neighbor]
			next_node.set_discovered()
			undiscovered_neighbors.remove(next_node)
			self.maze.undiscovered.remove(next_node)
			#then store the other neighbors in the queue and the copy of the maze
			for node in undiscovered_neighbors:
				if node not in self.maze.undiscovered:
					self.maze.undiscovered.append(node)
				self.undiscovered.put(node)
				
			#then get the path to the node
			self.goal = next_node
			return self.ASTAR(current_node,next_node)
			
		#otherwise we have to look back at what the agent missed
		else:
			if self.undiscovered.empty() == False:
				#pop the first thing off the queue
				#this is the most recent undiscovered node which should be the most efficient node to get to.
				next_node = self.undiscovered.get()
				#print next_node.pos 
				next_node.set_discovered()
				self.goal = next_node
				#print self.maze.undiscovered
				self.maze.undiscovered.remove(next_node)
				return self.ASTAR(current_node,next_node)
			else:
				#otherwise the discovery is done or if in a swarm you have to share across queues
				return False
				
	def ASTAR(self,start,end):
		closed_set = []
		open_set = [start]
		came_from = []
		
		#compute values for starting node
		#g_score is the distance from the start
		start.g_A = 0
		
		#h_score is purely heuristic, for this case we use manhattan distance
		self.h_score(start,start,end)
		
		#f_score is g_score + h_score
		self.f_score(start)
		
		#loop until all nodes are evaluated
		while len(open_set) != 0:
			#pick the most recent node in the set of untouched nodes
			#find the one that has the lowest f score
			current = open_set[0]
			for node in open_set:
				if node.f_A < current.f_A:
					current = node
					
			#if you are at the end create the path 
			if current == end:
				return self.reconstruct(came_from,current)
				
			open_set.remove(current)
			closed_set.append(current)
			
			#create list of neighbors
			neighbors = []
			for key1,key2 in current.edges:
				neighbors.append(self.maze.maze[(key1,key2)])
			
			for node in neighbors:
				#just keep going if already tested
				if node in closed_set:
					continue
					
				#compute a g_score for potiential candidate
				temp_g = current.g_A + current.edges[node.pos]
				
				#if it hasnt been seen yet mark for discovery
				if node not in open_set:
					open_set.append(node)
				#if we computed a worse g_score dont bother
				elif temp_g >= node.g_A:
					continue
				
				#otherwise we found a part of the path
				came_from.append(current)
				node.g_A = temp_g
				self.h_score(node,node,end)
				self.f_score(node) 
		
	#heuristic for the distance between two points, called manhattan distance
	def h_score(self,node,a,b):
		node.h_A = abs(a.pos[0] - b.pos[0])+abs(a.pos[1] - b.pos[1])
		
	def f_score(self,node):
		node.f_A = node.g_A + node.h_A
		
	def reconstruct(self,came_from,current_node):
		self.path = [current_node]
		for node in came_from:
			self.path.append(node)
			
		#self.path = self.path[::-1]
		return self.path