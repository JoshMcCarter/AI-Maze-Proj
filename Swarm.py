# File: Swarm.py
# Course: CMSC 471
# Assignment: Final Project
# Last Modified: 12/1/2018
# Description:
# This file contains the swarm algorithm implementations for managing multiple
# agents in a single maze. One cycle is defined as each agent updating their
# version of the maze, individually selecting a target node and path, checking
# with other agents to avoid collisions and target sharing, then moving to the
# desired location.


# Distance()
# Returns length of the path between two given positions
# Takes in two tuples, position a, and position b
def Distance(pos_a, pos_b):
    return #TODO return a path length between two positions


# SimpleCycle()
# Completes one cycle given N agents and the master maze for reference.
# Cycle Steps:
#   1. Each agent updates their map the the discoveries of other agents
#   2. Each agent decides where their next move location will be
#   3. Handle next-cycle collisions between agents
#   4. Handle target sharing between agents
#   5. Complete steps 3 and 4 until all conditions for success are met
#   6. Each agent moves in the maze and updates the 'master' with their pos.
def SimpleCycle(agents, master_map):

    # 1. Each agent updates their map with the discoveries of other agents
    # 2. Each agent decides where their next move location will be
    # 3. Handle next-cycle collisions between agents
    # 4. Handle target sharing between agents
    # 5. Complete steps 3 and 4 until all conditions for success are met
    # 6. Each agent moves in the maze and updates the 'master' with their pos.


# RDPSOCycle()
# Completes one cycle of the Robotic Darwinian Particle Swarm Optimization
def RDPSOCycle(agents, master_map):


# EPSOCycle()
# Completes one cycle of the Extended Particle Swarm Optimization Algorithm
# This algorithm compares each agent against the activities of its neighbor within some defined radius
# Agent paths outside that radius will not effect the given agent's activities
def EPSOCycle(agents, master_map, radius):

    # Evaluate robot individual solution

    # Share information with nearby neighbors

    # If Robots solution does not cause problems with nearby neighbors
        # robot is good to go

    # Build a vector H containing the individual solutions of all neighbors

    # if total solution is good, we are good
    # else, can we modify total solution, loop until solution is good
    # solution is used to avoid strong future collisions?

    # move



# PPSOCycle()
# agents: list of instantiated agents with pre-populated current positions
# master_map: master copy of the map to be updated by the individual agents
# Completes one cycle of the Physically-embedded Particle Swarm Optimization Algorithm
# DESC: This algorithm iterates through solutions until optimal solution is met
# Optimal Solution Descriptions:
# No Target Sharing
# No other agent is closer to any given agent's target, unless there is no better target choice
# No next-move collisions between agents
# Others?
def PPSOCycle(agents, master_map):
    ready_to_move = False

    # Conditional loop, loops until best solution for all agents is found
    while (ready_to_move == False):
        num_bad_conditions = 0 # number of issues with the next cycle to resolve

        for agent in agents:
            for check_agent in agents:

                # check for shared targets
                if (agent.goal == check_agent.goal):
                    # find the furthest of the two agents and tell it to rediscover
                    if (Distance(agent.goal, agent.current_pos) > Distance(check_agent.goal, check_agent.current_pos)):
                        agent.discover()
                    else:
                        check_agent.discover()
                    num_bad_conditions += 1

                # check for target swapping, if two agents are closer to eachothers goals than their own
                elif (Distance(agent.goal, check_agent.current_pos) < Distance(agent.goal, agent.current_pos)) and (Distance(check_agent.goal, agent.current_pos) < Distance(check_agent.goal, agent.current_pos)):
                    agent.goal, check_agent.goal = check_agent.goal, agent.goal

                    num_bad_conditions += 1
                    #TODO add re-pathing because the goals have been swapped but no the goals

                # check for next-move collisions
                # is there going to be a glance collision and has it not already been solved (one of the agents is paused)
                elif ():
                    # insert wait on one agent
                    num_bad_conditions += 1

                # is there going to be a crash collision
                elif (): #TODO will target swapping get rid of this?
                    # they need to move or they need to swap targets
                    num_bad_conditions += 1

                # is there a bottleneck collision forming
                elif ():
                    # berp
                    num_bad_conditions += 1

        # if current solution looks good, finish loop
        if (num_bad_conditions == 0):
            ready_to_move = True

    # Move
    change_queue = []
    for agent in agents:
        # queue up changes for updates to mazes
        agent.move() # needs PATH variable!!

    # apply updates to the mazes
    for change in change_queue:
        for


# GSOCycle()
# Completes one cycle of the Glow-worm Swarm Optimization Algorithm
def GSOCycle(agents, master_map):