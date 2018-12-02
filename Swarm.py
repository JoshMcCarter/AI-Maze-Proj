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
def EPSOCycle(agents, master_map):



# PPSOCycle()
# agents: list of instantiated agents with pre-populated current positions
# master_map: master copy of the map to be updated by the individual agents
# Completes one cycle of the Physically-embedded Particle Swarm Optimization Algorithm
# DESC: This algorithm iterates through solutions until optimal solution is met
def PPSOCycle(agents, master_map):
    ready_to_move = False

    # Conditional loop, loops until best solution for all agents is found
    while (ready_to_move == False):
        num_bad_conditions = 0 # number of issues with the next cycle to resolve

        # check for shared targets
        if ():
            # shared target found
            # mark Agent further from target for re-discovery
            # num_bad_conditions ++

        # check for target swaps (is one closer to a target than the other?)
        if ():

        # check for next-move collisions
        if ():
            # is it a one turn (intersection) collision? 50% chance for who waits one cycle
            # does one need to move to allow the other to pass?
                # swap targets so they just change directions
            # is the agent inactive? if so just ask that one to move, assign temporary target

        # if current solution looks good, finish loop
        if (num_bad_conditions == 0):
            ready_to_move = True

    # Move
    for agent in agents:
        agent.move() # needs PATH variable!!

    # update maze with new agent locations and targets?


# GSOCycle()
# Completes one cycle of the Glow-worm Swarm Optimization Algorithm
def GSOCycle(agents, master_map):