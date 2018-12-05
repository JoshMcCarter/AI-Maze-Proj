# Test 1 for Swarm AI
# Single row, swap target test
# PASSED with 2 Agents
# PPSOCycle

from Node import Node
from OldMaze import Maze
from Agent import Agent
from Swarm import PPSOCycle


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

node1 = Node(False,False,False,False,(0, 5), False)
node2 = Node(False,False,False,False,(0, 4), True)
node3 = Node(False,False,False,False,(0, 3), True)
node4 = Node(False,False,False,False,(0, 2), True)
node5 = Node(False,False,False,False,(0, 1), True)
node6 = Node(False,False,False,False,(0, 0), False)
node1.set_down(node2)
node2.set_up(node1)
node2.set_down(node3)
node3.set_up(node2)
node3.set_down(node4)
node4.set_up(node3)
node4.set_down(node5)
node5.set_up(node4)
node5.set_down(node6)
node6.set_up(node5)

nodes = [node1, node2, node3, node4, node5, node6]

foo = Maze(nodes)
agent1 = Agent(node4,foo)
agent2 = Agent(node3,foo)
agents = [agent1, agent2]

print("Begin maze")
print("Agent 1 location: ", agent1.current_pos)
print("Agent 2 location: ", agent2.current_pos)

while not check_win_condition(agents):
    input(">>> Press enter to continue")
    PPSOCycle(agents)
    PrintAgent(agents[0], 1)
    PrintAgent(agents[1], 2)

print("Maze fully Discovered!")
