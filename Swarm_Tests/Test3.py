# Test 1 for Swarm AI
# L Maze
# PPSOCycle

from Node import Node
from Maze import Maze
from Agent import Agent
from Swarm import PPSOCycle


def PrintAgent(agent, agent_num):
    print("*** AGENT", agent_num)
    print("  Current Position:", agent.current_pos)
    if (len(agent.path) != 0):
        print("  Path:", agent.path[0])
    else:
        print("  Path: NONE")
#     print("  Goal:", agent.goal.pos)
    print("")



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
agent1 = Agent(node1,foo)
agent2 = Agent(node4,foo)
agents = [agent1, agent2]

print("Begin maze")
print("Agent 1 location: ", agent1.current_pos)
print("Agent 2 location: ", agent2.current_pos)


while(len(agent1.maze.undiscovered) > 0):
    input(">>> Press enter to continue")
    PPSOCycle(agents)
    PrintAgent(agents[0], 1)
    PrintAgent(agents[1], 2)

print("Maze fully Discovered!")
