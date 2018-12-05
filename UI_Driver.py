# CMSC 471
# AI Final Project
# UI Enabled Driver

# Imports
from Maze import Maze
from Agent import Agent
from Swarm import PPSOCycle
from OLD_UI import UserInterface
import random
import sys


def main(input_arguments):
    # verify number of command line arguments
    if input_arguments[-1].upper() == "DEBUG":
        debug = True
    else:
        debug = False

    # check swarm algorithm variable
    swarm_algorithm = input_arguments[3].upper()
    if swarm_algorithm != "PPSO" and swarm_algorithm != "EPSO":
        print("Invalid Swarm algorithm. Choices are: PPSO, EPSO")
        return 1

    if swarm_algorithm == "EPSO":
        radius = int(input_arguments[4])
    else:
        radius = 0

    # get number of agents:
    num_agents = input_arguments[2]

    # verify maze file exists
    maze_filename = input_arguments[1]

    # load maze from selected file
    print("Loading Maze from file", maze_filename, "...")
    maze = Maze(maze_filename)
    maze.debug = debug

    # make agents here
    agents = []
    for x in range(int(num_agents)):
        random_node = random.choice(maze.undiscovered)  # select random node
        maze.undiscovered.remove(random_node)
        agents.append(Agent(random_node, maze))
        if maze.debug is True:
            print("    Agent", x, "initial location:", random_node.pos)

    # make UI here
    cycle_statistics = []

    # call UI
    ui = UserInterface(maze, agents, cycle_statistics, maze_filename)

# End of loop
    print("\n *** Maze Discovery Complete *** ")


# CHANGE VALUES HERE FOR CHANGE OF WHAT IT DOES
main(["UI_Driver.py", "Maze_Generation\Mazes\\tinymazes\\tinymaze1600_2.txt", "2", "PPSO"])

