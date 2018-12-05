# Test 2 for Swarm AI
# Square Maze
# PPSOCycle

from Node import Node
from OldMaze import Maze
from Agent import Agent
from Swarm import PPSOCycle
import random

def PrintAgent(agent, agent_num):
    print("*** AGENT", agent_num)
    print("  Current Position:", agent.current_pos)
    if (len(agent.path) > 0):
        for i in agent.path:
            print("<", i.pos, "> ", end='')
        print("")
    else:
        print("  Path: NONE")
    print("  Goal:", agent.goal.pos)
    print("")
    print("Remaining Undiscovered Nodes:")
    for temp_val in agent.maze.undiscovered:
        print(temp_val.pos, end='')
    print("")

def check_win_condition(agents):
    # check if there are undiscovered nodes
    if len(agents[0].maze.undiscovered) > 0:
        return False

    # check if all undiscovered nodes have been reached
    for agent in agents:
        if agent.goal != agent.current_node:
            return False

    return True

node1 = Node(False,False,False,False,(0,0),True)
node2 = Node(False,False,False,False,(0,1),False)
node3 = Node(False,False,False,False,(0,2),False)
node4 = Node(False,False,False,False,(1,2),False)
node5 = Node(False,False,False,False,(2,2),True)
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

nodes = [node1,node2,node3,node4,node5,node6,node7,node8, node9]

foo = Maze(nodes)
num_agents = 2
agents = []
for x in range(num_agents):
    random_node = random.choice(foo.undiscovered)  # select random node
    foo.undiscovered.remove(random_node)
    agents.append(Agent(random_node, foo))

print("Begin maze")
print("Agent 1 location: ", agents[0].current_pos)
print("Agent 2 location: ", agents[1].current_pos)

while not check_win_condition(agents):
    input(">>> Press enter to continue")
    PPSOCycle(agents)
    PrintAgent(agents[0], 1)
    PrintAgent(agents[1], 2)

print("Maze fully Discovered!")
