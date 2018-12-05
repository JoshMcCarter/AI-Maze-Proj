# CMSC 471
# Team #3
# Josh McCarter, Alex Miu, Jack Wang, Itay Tamary
# Main Driver for Final AI Project

# Imports
import random
import sys
import os
import time
from Maze import Maze
from Swarm import PPSOCycle, EPSOCycle
from Agent import Agent


def print_agent(agent, agent_num):
    print("*** AGENT", agent_num)
    print("  Current Position:", agent.current_pos)
    if len(agent.path) > 0:
        print("  Path: ", end='')
        for i in agent.path:
            print("<" + str(i.pos) + "> ", end='')
        print("")
    else:
        print("  Path: NONE")
    if agent.goal:
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


def run_maze(maze_filename, num_agents, swarm_algorithm, enable_debug, radius=0):

    # load maze from selected file
    print("Loading Maze from file", maze_filename, "...")
    maze = Maze(maze_filename)
    maze.debug = enable_debug

    # place agents in maze
    print("Generating Agents ...")
    agents = []
    for x in range(num_agents):
        random_node = random.choice(maze.undiscovered)  # select random node
        maze.undiscovered.remove(random_node)
        agents.append(Agent(random_node, maze))

        if maze.debug is True:
            print("    Agent", x, "initial location:", random_node.pos)

    cycle_statistics = []
    single_step = True
    num_cycles = 0
    # loop through until maze is solved
    while not check_win_condition(agents):

        # debug instructions for loop
        if maze.debug is True and single_step:
            for x in range(num_agents):
                print_agent(agents[x], x)

            print("Remaining Undiscovered Nodes:", end='')
            for temp_val in maze.undiscovered:
                print(temp_val.pos, end='')

            print("")
            temp1 = input("\n>>> Press ENTER to continue or type 'continue' to disable single_step: ")
            if temp1.lower() == "continue":
                single_step = False

        if swarm_algorithm == "PPSO":
            cycle_statistics.append(PPSOCycle(agents))
        else:  # use EPSOCycle
            cycle_statistics.append(EPSOCycle(agents, radius))
        num_cycles += 1

    # End of loop
    print("\n *** Maze Discovery Complete *** ")

    # if debug enabled, print cycle statistics
    if maze.debug is True:
        for index_val in range(len(cycle_statistics)):
            print("\n >>> CYCLE", index_val + 1, "REPORT:")
            for incident in cycle_statistics[index_val]:
                print("* EVENT:")
                print("    Type:", incident[0])
                print("    Location:", incident[1])
                if incident[0] == "SWAPPING_TARGETS":
                    print("    Location:", incident[2])

    # Write statistics to output file
    # Line Format: num_agents,radius,num_nodes,cycle_num,num_undiscovered,incident_type,incident_location
    output_filename = maze_filename.split(".")[0] + "_OUTPUT.csv"
    print("Appending cycle statistics to output file:", output_filename)
    out_file_handle = open(output_filename, 'a')
    for index_val in range(len(cycle_statistics)):
        for incident in cycle_statistics[index_val]:
            if incident[0] == "SWAPPING_TARGETS":
                out_file_handle.write(str(num_agents) + "," + str(radius) + "," + str(len(maze.nodes)) + "," + str(index_val + 1) + "," + str(len(maze.undiscovered)) + ",\"" + incident[0] + "\",\"" + str(incident[1]) + "\"" + str(incident[2]) + "\"\n")
            else:
                out_file_handle.write(str(num_agents) + "," + str(radius) + "," + str(len(maze.nodes)) + "," + str(index_val + 1) + "," + str(len(maze.undiscovered)) + ",\"" + incident[0] + "\",\"" + str(incident[1]) + "\"\n")
    out_file_handle.write("TOTAL_CYCLES," + str(num_cycles) + "\n")
    out_file_handle.close()
    # END OF FUNCTION


# Driver usage:
# python Driver.py maze_file_path max_agents PPSO
# python Driver.py maze_file_path max_agents EPSO radius
# python Driver.py maze_file_path max_agents swarm [radius] debug
def main(input_arguments):

    # verify number of command line arguments
    if input_arguments[-1].upper() == "DEBUG":
        debug = True
    else:
        debug = False

    # check swarm algorithm variable
    swarm_algorithm = input_arguments[2].upper()
    if swarm_algorithm != "PPSO" and swarm_algorithm != "EPSO":
        print("Invalid Swarm algorithm. Choices are: PPSO, EPSO")
        return 1

    if swarm_algorithm == "EPSO":
        radius = int(input_arguments[3])
    else:
        radius = 0

    # get number of agents:
    num_agents = input_arguments[1]

    # verify maze file exists
    maze_filename = input_arguments[0]

    # Run through program with various agents
    if swarm_algorithm == "PPSO":
        for i in range(1, int(num_agents)):
            run_maze(maze_filename, i, swarm_algorithm, debug)

    else:
        for i in range(1, int(num_agents)):
            for r in range(2, int(radius)):
                run_maze(maze_filename, i, swarm_algorithm, debug, radius)


# Run function
#start_time = time.time()
#main(sys.argv)
#print("----------%s seconds----------" % (time.time() - start_time))
