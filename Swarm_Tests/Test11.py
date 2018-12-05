# Test 11 for Swarm AI
# Path Test
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


node1 = Node(False,False,False,False,(0, 0), False)
node2 = Node(False,False,False,False,(0, 1), True)
node3 = Node(False,False,False,False,(0, 2), True)
node4 = Node(False,False,False,False,(0, 3), True)
node5 = Node(False,False,False,False,(0, 4), True)
node6 = Node(False,False,False,False,(0, 5), True)
node7 = Node(False,False,False,False,(0, 6), True)
node8 = Node(False,False,False,False,(0, 7), True)
node9 = Node(False,False,False,False,(0, 8), True)
node10 = Node(False,False,False,False,(0, 9), True)
node11 = Node(False,False,False,False,(0, 10), True)
node12 = Node(False,False,False,False,(0, 11), True)
node13 = Node(False,False,False,False,(0, 12), True)
node14 = Node(False,False,False,False,(0, 13), True)
node15 = Node(False,False,False,False,(0, 14), True)

node1.set_up(node2)
node2.set_down(node1)
node2.set_up(node3)

node3.set_down(node2)
node3.set_up(node4)

node4.set_down(node3)
node4.set_up(node5)

node5.set_down(node4)
node5.set_up(node6)

node6.set_down(node5)
node6.set_up(node7)

node7.set_down(node6)
node7.set_up(node8)

node8.set_down(node7)
node8.set_up(node9)

node9.set_down(node8)
node9.set_up(node10)

node10.set_down(node9)
node10.set_up(node11)

node11.set_down(node10)
node11.set_up(node12)

node12.set_down(node11)
node12.set_up(node13)

node13.set_down(node12)
node13.set_up(node14)

node14.set_down(node13)
node14.set_up(node15)

node15.set_down(node14)

nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15]

foo = Maze(nodes)
agent1 = Agent(node15,foo)

agents = [agent1]

print("Begin maze")
print("Agent 1 location: ", agent1.current_pos)
# print("Agent 2 location: ", agent2.current_pos)

while not check_win_condition(agents):
    input(">>> Press enter to continue")
    PPSOCycle(agents)
    PrintAgent(agents[0], 0)
    # PrintAgent(agents[1], 1)

print("Maze fully Discovered!")
