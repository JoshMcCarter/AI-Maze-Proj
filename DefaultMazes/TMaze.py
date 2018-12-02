from Node import Node
from Maze import Maze
from Agent import Agent

node1 = Node(False,False,False,False,(0,0),False)
node2 = Node(False,False,False,False,(0,1),False)
node3 = Node(False,False,False,False,(1,1),False)
node4 = Node(False,False,False,False,(-1,1),False)
node1.set_up(node2)
node2.set_down(node1)
node2.set_left(node4)
node2.set_right(node3)
node3.set_left(node2)
node4.set_right(node2)

nodes = [node1,node2,node3,node4]

foo = Maze(nodes)

agent = Agent((0,0),foo)
agent.simple_discovery()
print foo.undiscovered
print agent.current_pos