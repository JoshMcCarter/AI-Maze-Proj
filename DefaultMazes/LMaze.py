from Node import Node
from Maze import Maze
from Agent import Agent

node1 = Node(False,False,False,False,(0,0),False)
node2 = Node(False,False,False,False,(0,-1),False)
node3 = Node(False,False,False,False,(0,-2),False)
node4 = Node(False,False,False,False,(0,-3),False)
node5 = Node(False,False,False,False,(1,-3),False)
node1.set_down(node2)
node2.set_down(node3)
node3.set_down(node4)
node4.set_right(node5)
node2.set_up(node1)
node3.set_up(node2)
node4.set_up(node3)
node5.set_left(node4)

nodes = [node1,node2,node3,node4,node5]

foo = Maze(nodes)
agent = Agent((0,0),foo)
agent.simple_discovery()
print agent.current_pos