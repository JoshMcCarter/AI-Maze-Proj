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
# Returns manhattan distance between two given positions
# Takes in two tuples, position a, and position b
def Distance(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])

# EPSOCycle()
# Completes one cycle of the Extended Particle Swarm Optimization Algorithm
# This algorithm compares each agent against the activities of its neighbor within some defined radius
# Agent paths outside that radius will not effect the given agent's activities
# TODO Implement this one
# def EPSOCycle(agents, master_map, radius):

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
# Completes one cycle of the Physically-embedded Particle Swarm Optimization Algorithm
# DESC: This algorithm iterates through solutions until optimal solution is met
# Optimal Solution Descriptions:
# No Target Sharing
# No other agent is closer to any given agent's target, unless there is no better target choice
# No next-move collisions between agents
# Others?
def PPSOCycle(agents):
    ready_to_move = False
    agents_that_move = [1] * len(agents)

    # Check for agents completed with their paths, ensures every agent has a path if there are enough undiscovered locations
    for agent_index in range(len(agents)):
        if (len(agents[agent_index].path) == 0) and (len(agents[agent_index].maze.undiscovered) >= len(agents)):
            agents[agent_index].discover(agents[agent_index].current_node)
        elif (len(agents[agent_index].path) == 0):
            # there arent enough positions, this agent doesn't move
            agents_that_move[agent_index] = 0

    # Conditional loop, loops until best solution for all agents is found
    while (ready_to_move == False):
        num_bad_conditions = 0 # number of issues with the next cycle to resolve
        outer_agent_moving_index = 0
        for agent in agents:
            moving_index = 0
            for check_agent in agents:

                # only look at agent if it is active and is not paused
                if len(check_agent.path) > 0 and agents_that_move[moving_index] == 1:

                    #***** CHECK FOR COLLISIONS
                    # is there someone in the next node
                    if (check_agent.path[0].agent_on == True):
                        num_bad_conditions += 1
                        # if they intend to move, go ahead
                            # DON'T NEED TO MODIFY ANYTHING
                        # if they are paused due to inactivity, swap targets with them, you become inactive
                        if (agents_that_move[outer_agent_moving_index] == 0) and (len(agent.path) == 0):
                            agent.ASTAR(agent.current_pos, check_agent.path[-1])
                            agents_that_move[outer_agent_moving_index] = 1

                            check_agent.path = []
                            agents_that_move[moving_index] = 0

                        # if they are paused for one turn, you pause too
                        elif (agents_that_move[outer_agent_moving_index] == 0) and (len(agent.path) > 0):
                            agents_that_move[moving_index] = 0

                    # is there going to be a collision where they move into the same spot
                    if (agents_that_move[outer_agent_moving_index] == 1):
                        if(agent.path[0] == check_agent.path[0]):
                            num_bad_conditions += 1
                            agents_that_move[outer_agent_moving_index] = 0

                    #***** CHECK FOR TARGET CHANGE IF BOTH AGENTS ARE ACTIVE
                    if len(agent.path) > 0:

                        # check for shared targets
                        if (agent.goal == check_agent.goal):
                            # find the furthest of the two agents and tell it to rediscover
                            if (len(agent.path) > len(check_agent.path)):
                                agent.discover()
                            else:
                                    check_agent.discover()
                            num_bad_conditions += 1

                        # check for target swapping, if two agents are closer to eachothers goals than their own
                        if (Distance(agent.goal, check_agent.current_pos) < Distance(agent.goal, agent.current_pos)) and (Distance(check_agent.goal, agent.current_pos) < Distance(check_agent.goal, agent.current_pos)):
                            temp_goal = agent.path[-1]
                            agent.ASTAR(agent.current_node, check_agent.path[-1])
                            check_agent.ASTAR(check_agent.current_node, temp_goal)
                            num_bad_conditions += 1

                moving_index += 1
            outer_agent_moving_index += 1

        # if current solution looks good, finish loop
        if (num_bad_conditions == 0):
            ready_to_move = True

    # Move
    for cur_agent_index in range(len(agents)):
        if (agents_that_move[cur_agent_index] == 1): # if agent is supposed to move this cycle
            agents[cur_agent_index].move(agents[cur_agent_index].path)



# GSOCycle()
# Completes one cycle of the Glow-worm Swarm Optimization Algorithm
# TODO Implement this one
# def GSOCycle(agents, master_map):