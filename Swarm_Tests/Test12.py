# Test 9 for Swarm AI
# 4 Agent simple test
# Hollow Square Maze
#
# PPSOCycle


# TODO this file is not done

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

def check_win_condition(agents):
    # check if there are undiscovered nodes
    if len(agents[0].maze.undiscovered) > 0:
        return False

    # check if all undiscovered nodes have been reached
    for agent in agents:
        if agent.goal != agent.current_node:
            return False

    return True


node1 = Node(False,False,False,False,(0, 0), True)
node2 = Node(False,False,False,False,(0, 1), False)
node3 = Node(False,False,False,False,(0, 2), False)
node4 = Node(False,False,False,False,(0, 3), True)
node5 = Node(False,False,False,False,(1, 0), False)
node6 = Node(False,False,False,False,(1, 3), False)
node7 = Node(False,False,False,False,(2, 0), False)
node8 = Node(False,False,False,False,(2, 3), False)
node9 = Node(False,False,False,False,(3, 0), True)
node10 = Node(False,False,False,False,(3, 1), False)
node11 = Node(False,False,False,False,(3, 2), False)
node12 = Node(False,False,False,False,(3, 3), True)
node13 = Node(False,False,False,False,(1, 1), False)
node14 = Node(False,False,False,False,(1, 2), False)
node15 = Node(False,False,False,False,(2, 1), False)
node16 = Node(False,False,False,False,(2, 2), True)

node14.set_up(node6)
node14.set_down(node13)
node14.set_left(node1)

node13.set_up(node14)
node13.set_down(node5)
node13.set_left(node2)
node13.set_right(node15)

node11.set_left(node16)
node10.set_left(node15)
node8.set_down(node16)
node7.set_up(node15)
node1.set_up(node2)
node1.set_right(node5)
node2.set_down(node1)
node2.set_right(node13)
node2.set_up(node3)
node3.set_down(node2)
node3.set_right(node14)
node3.set_up(node4)
node4.set_down(node3)
node4.set_right(node6)
node6.set_left(node4)
node6.set_right(node8)
node6.set_down(node14)
node8.set_left(node6)
node8.set_right(node12)
node12.set_left(node8)
node12.set_down(node11)
node11.set_up(node12)
node11.set_down(node10)
node10.set_up(node11)
node10.set_down(node9)
node9.set_up(node10)
node9.set_left(node7)
node7.set_right(node9)
node7.set_left(node5)
node5.set_right(node7)
node5.set_left(node1)
node5.set_up(node13)

nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12]

foo = Maze(nodes)
agent1 = Agent(node1, foo)
agent2 = Agent(node4, foo)
agent3 = Agent(node9, foo)
agent4 = Agent(node12, foo)

agents = [agent1, agent2, agent3, agent4]

print("Begin maze")
print("Agent 0 location: ", agent1.current_pos)
print("Agent 1 location: ", agent2.current_pos)
print("Agent 2 location: ", agent3.current_pos)
print("Agent 3 location: ", agent4.current_pos)

while not check_win_condition(agents):
    input(">>> Press enter to continue")
    PPSOCycle(agents)
    PrintAgent(agents[0], 0)
    PrintAgent(agents[1], 1)
    PrintAgent(agents[2], 2)
    PrintAgent(agents[3], 3)

    print("Remaining Undiscovered Nodes:")
    for temp_val in agents[0].maze.undiscovered:
        print(temp_val.pos, end='')
    print("")

print("Maze fully Discovered!")
