# CMSC 471
# AI Final Project
# UI Enabled Driver

# Imports
from Node import Node
from OldMaze import Maze
from Agent import Agent
from Swarm import PPSOCycle
from UI import UserInterface
import random

def check_win_condition(agents):
    # check if there are undiscovered nodes
    if len(agents[0].maze.undiscovered) > 0:
        return False

    # check if all undiscovered nodes have been reached
    for agent in agents:
        if agent.goal != agent.current_node:
            return False

    return True


def main():
    num_agents = 2
    # input_filename = "Maze_Generation\\Mazes\\tinymazes\\tinymaze1600_1.txt"
    # maze1 = Maze(input_filename)
    print("start")
    node1 = Node(False, False, False, False, (0, 2), True)
    node2 = Node(False, False, False, False, (0, 1), False)
    node3 = Node(False, False, False, False, (0, 0), False)
    node4 = Node(False, False, False, False, (1, 0), False)
    node5 = Node(False, False, False, False, (2, 0), True)
    node6 = Node(False, False, False, False, (2, 1), False)
    node7 = Node(False, False, False, False, (2, 2), False)
    node8 = Node(False, False, False, False, (1, 2), False)
    node9 = Node(False, False, False, False, (1, 1), False)
    node10 = Node(False, False, False, False, (1, 3), False)
    node11 = Node(False, False, False, False, (1, 4), False)
    node12 = Node(False, False, False, False, (1, 5), False)
    node13 = Node(False, False, False, False, (1, 6), False)
    node14 = Node(False, False, False, False, (1, 7), False)
    node15 = Node(False, False, False, False, (1, 8), False)
    node16 = Node(False, False, False, False, (1, 9), False)
    node17 = Node(False, False, False, False, (1, 10), False)
    node18 = Node(False, False, False, False, (1, 11), False)
    node19 = Node(False, False, False, False, (1, 12), False)
    node20 = Node(False, False, False, False, (1, 13), False)
    node21 = Node(False, False, False, False, (1, 14), False)
    node22 = Node(False, False, False, False, (1, 15), False)
    node23 = Node(False, False, False, False, (1, 16), False)
    node24 = Node(False, False, False, False, (1, 17), False)
    node25 = Node(False, False, False, False, (1, 18), False)
    node26 = Node(False, False, False, False, (1, 19), False)
    node27 = Node(False, False, False, False, (1, 20), False)
    node28 = Node(False, False, False, False, (1, 21), False)
    node29 = Node(False, False, False, False, (1, 22), False)
    node30 = Node(False, False, False, False, (1, 23), False)
    node31 = Node(False, False, False, False, (1, 24), False)
    node32 = Node(False, False, False, False, (1, 25), False)
    node33 = Node(False, False, False, False, (1, 26), False)
    node34 = Node(False, False, False, False, (1, 27), False)
    node35 = Node(False, False, False, False, (1, 28), False)
    node36 = Node(False, False, False, False, (1, 29), False)
    node37 = Node(False, False, False, False, (1, 30), False)
    node38 = Node(False, False, False, False, (1, 31), False)
    node39 = Node(False, False, False, False, (1, 32), False)
    node40 = Node(False, False, False, False, (1, 33), False)
    node41 = Node(False, False, False, False, (1, 34), False)
    node42 = Node(False, False, False, False, (1, 35), False)
    node43 = Node(False, False, False, False, (1, 36), False)
    node44 = Node(False, False, False, False, (1, 37), False)
    node45 = Node(False, False, False, False, (1, 38), False)
    node46 = Node(False, False, False, False, (1, 39), False)
    node47 = Node(False, False, False, False, (1, 40), False)
    node48 = Node(False, False, False, False, (1, 11), False)

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
    node8.set_down(node10)
    node10.set_up(node8)
    node10.set_down(node11)
    node11.set_up(node10)
    node11.set_down(node12)
    node12.set_up(node11)
    node12.set_down(node13)
    node13.set_up(node12)
    node13.set_down(node14)
    node14.set_up(node13)
    node14.set_down(node15)
    node15.set_up(node14)
    node15.set_down(node16)
    node16.set_up(node15)
    node16.set_down(node17)
    node17.set_up(node16)
    node17.set_down(node18)
    node18.set_up(node17)
    node18.set_down(node19)
    node19.set_up(node18)
    node19.set_down(node20)
    node20.set_up(node19)
    node20.set_down(node21)
    node21.set_up(node20)
    node21.set_down(node22)
    node22.set_up(node21)
    node22.set_down(node23)
    node23.set_up(node22)
    node23.set_down(node24)
    node24.set_up(node23)
    node24.set_down(node25)
    node25.set_up(node24)
    node25.set_down(node26)
    node26.set_up(node25)
    node26.set_down(node27)
    node27.set_up(node26)
    node27.set_down(node28)
    node28.set_up(node27)
    node28.set_down(node29)
    node29.set_up(node28)
    node29.set_down(node30)
    node30.set_up(node29)
    node30.set_down(node31)
    node31.set_up(node30)
    node31.set_down(node32)
    node32.set_up(node31)
    node32.set_down(node33)
    node33.set_up(node32)
    node33.set_down(node34)
    node34.set_up(node33)
    node34.set_down(node35)
    node35.set_up(node34)
    node35.set_down(node36)
    node36.set_up(node35)
    node36.set_down(node37)
    node37.set_up(node36)
    node37.set_down(node38)
    node38.set_up(node37)
    node38.set_down(node39)
    node39.set_up(node38)
    node39.set_down(node40)
    node40.set_up(node39)
    node40.set_down(node41)
    node41.set_up(node40)
    node41.set_down(node42)
    node42.set_up(node41)
    node42.set_down(node43)
    node43.set_up(node42)
    node43.set_down(node44)
    node44.set_up(node43)
    node44.set_down(node45)
    node45.set_up(node44)
    node45.set_down(node46)
    node46.set_up(node45)
    node46.set_down(node47)
    node47.set_up(node46)
    node47.set_down(node48)
    node48.set_up(node47)
    print("1")
    nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15, node16, node17, node18, node19, node20, node21, node22, node23, node24, node25, node26, node27, node28, node29, node30, node31, node32, node33, node34, node35, node36, node37, node38, node39, node40, node41, node42, node43, node44, node45, node46, node47, node48]
    maze1 = Maze(nodes)

    # make agents here
    agents = []
    for x in range(num_agents):
        random_node = random.choice(maze1.undiscovered)  # select random node
        maze1.undiscovered.remove(random_node)
        agents.append(Agent(random_node, maze1))

    # make UI here
    ui = UserInterface(maze1, agents)

main()
