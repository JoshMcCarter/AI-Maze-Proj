from Node import Node
from Maze import Maze
from Agent import Agent

node1 = Node(False,False,False,False,(0,0),False)
node2 = Node(False,False,False,False,(0,1),False)
node3 = Node(False,False,False,False,(0,2),False)
node4 = Node(False,False,False,False,(1,2),False)
node5 = Node(False,False,False,False,(2,2),False)
node6 = Node(False,False,False,False,(2,1),False)
node7 = Node(False,False,False,False,(2,0),False)
node8 = Node(False,False,False,False,(1,0),False)
node9 = Node(False,False,False,False,(1,1),False)

node1.set_up(node2)
node1.set_right(node8)
node2.set_down(node1)
node2.set_up(node3)
node3.set_down(node2)
node3.set_right(node4)
node4.set_left(node3)
node4.set_right(node5)
node5.set_left(node4)
node5.set_down(node6)
node6.set_up(node5)
node6.set_down(node7)
node7.set_left(node8)
node7.set_up(node6)
node8.set_right(node7)
node8.set_left(node1)
node4.set_down(node9)
node9.set_up(node4)

nodes = [node1,node2,node3,node4,node5,node6,node7,node8,node9]

foo = Maze(nodes)

agent = Agent((0,0),foo)
agent.simple_discovery()
print foo.undiscovered
print agent.current_pos