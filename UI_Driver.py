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

    node1 = Node(False, False, False, False, (0, 0), True)
    node2 = Node(False, False, False, False, (0, 1), False)
    node3 = Node(False, False, False, False, (0, 2), False)
    node4 = Node(False, False, False, False, (1, 2), False)
    node5 = Node(False, False, False, False, (2, 2), True)
    node6 = Node(False, False, False, False, (2, 1), False)
    node7 = Node(False, False, False, False, (2, 0), False)
    node8 = Node(False, False, False, False, (1, 0), False)
    node9 = Node(False, False, False, False, (1, 1), False)

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

    nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9]

    maze1 = Maze(nodes)

    # make agents here
    agents = []
    for x in range(num_agents):
        random_node = random.choice(maze1.undiscovered)  # select random node
        maze1.undiscovered.remove(random_node)
        agents.append(Agent(random_node, maze1))

    # make UI here
    ui = UserInterface(maze1, agents)
    print("Done setting up UI")

    # main loop
    while not check_win_condition(agents):

        if ui.one_step_flag > 0 and ui.pause_flag is False and ui.start_flag is True:
            PPSOCycle(agents)
            ui.update(maze1, agents)
            ui.one_step_flag -= 1

        if ui.start_flag is True and ui.pause_flag is False:
            PPSOCycle(agents)
            ui.update(maze1, agents)


main()
