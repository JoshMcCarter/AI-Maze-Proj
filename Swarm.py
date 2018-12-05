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
# Helper function
# Returns manhattan distance between two given positions
# Takes in two tuples, position a, and position b
def Distance(node_a, node_b):
    return abs(node_a.pos[0] - node_b.pos[0]) + abs(node_a.pos[1] - node_b.pos[1])

# EPSOCycle()
# Completes one cycle of the Extended Particle Swarm Optimization Algorithm
# This algorithm compares each agent against the activities of its neighbor within some defined radius
# Agent paths outside that radius will not effect the given agent's activities
# Same collision and target avoidance, except they only interact with agents within a certain radius
# INPUTS
#   agents: list of agents in maze
#   radius: max distance between agents allowed, minimum value required is 2 units, for collision checking
def EPSOCycle(agents, radius):
    ready_to_move = False

    agents_that_move = [1] * len(agents)

    # Check for agents completed with their paths,
    # ensures every agent has a path if there are enough undiscovered locations
    for agent_index in range(len(agents)):
        if ((len(agents[agent_index].path) == 0) or (agents[agent_index].goal == agents[agent_index].current_node)):
            agents[agent_index].path = agents[agent_index].discover(agents[agent_index].current_node)
            print(agents[agent_index].path)

            if agents[agent_index].path == False:
                # nothing in agent's queue, grab from large pool

                nearby_agents = []
                for agent_temp in agents:
                    if Distance(agents[agent_index].current_node, agent_temp.current_node) < radius:
                        nearby_agents.append(agent_temp)

                index_val = 0
                while (agents[agent_index].path == False) and (index_val < len(nearby_agents)):
                    if not nearby_agents[index_val].undiscovered.empty():
                        temp_goal = nearby_agents[index_val].undiscovered.get()
                        agents[agent_index].undiscovered.put(temp_goal)
                        agents[agent_index].maze.undiscovered.append(temp_goal)
                        agents[agent_index].path = agents[agent_index].discover(agents[agent_index].current_node)
                        print(agents[agent_index].path)

                else:
                    # deactivate agent, nowhere for it to go
                    agents[agent_index].path = []
                    agents[agent_index].goal = agents[agent_index].current_node
                    print("Deactivating agent", agent_index)
                    agents_that_move[agent_index] = 0

    # Conditional loop, loops until best solution for all agents is found
    while (ready_to_move == False):
        num_bad_conditions = 0  # number of issues with the next cycle to resolve
        outer_agent_moving_index = 0
        for agent in agents:
            moving_index = 0

            # build list of nearby agents
            nearby_agents = []
            for agent_temp in agents:
                if Distance(agent.current_node, agent_temp.current_node) < radius:
                    nearby_agents.append(agent_temp)

            # Only perform checks against agents in nearby radius
            for check_agent in nearby_agents:
                # only look at agent if it is active and is not paused and not itself
                if (agent != check_agent) and (len(check_agent.path) > 0) and (agents_that_move[moving_index] == 1):

                    # ***** CHECK FOR TARGET CHANGE IF BOTH AGENTS ARE ACTIVE
                    if len(agent.path) > 0:

                        # check for shared targets
                        if (agent.goal == check_agent.goal):
                            print("Duplicate targets!")
                            # find the furthest of the two agents and tell it to rediscover
                            if (len(agent.path) > len(check_agent.path)):
                                print("Path length case 1")
                                agent.path = agent.discover(agent.current_node)
                                if agent.path == False:
                                    # nothing in agent's queue, grab from large pool

                                    if len(agent.maze.undiscovered) > 0:
                                        print("Assigning new path to agent")
                                        agent.undiscovered.put(agent.maze.undiscovered[0])
                                        agent.path = agent.discover(agent.current_node)

                                    else:
                                        # deactivate agent, nowhere for it to go
                                        agent.path = []
                                        agent.goal = agent.current_node
                                        print("Deactivating agent", outer_agent_moving_index)
                                        agents_that_move[outer_agent_moving_index] = 0
                            else:
                                print("Path length case 2")
                                check_agent.path = check_agent.discover(check_agent.current_node)
                                if check_agent.path == False:
                                    # nothing in agent's queue, grab from large pool

                                    if len(check_agent.maze.undiscovered) > 0:
                                        print("Assigning new path to agent")
                                        check_agent.undiscovered.put(check_agent.maze.undiscovered[0])
                                        check_agent.path = check_agent.discover(check_agent.current_node)

                                    else:
                                        # deactivate agent, nowhere for it to go
                                        check_agent.path = []
                                        check_agent.goal = check_agent.current_node
                                        print("Deactivating agent", moving_index)
                                        agents_that_move[moving_index] = 0

                            num_bad_conditions += 1

                        # check for target swapping, if two agents are closer to eachothers goals than their own
                        if (Distance(agent.goal, check_agent.current_node) < Distance(agent.goal, agent.current_node)) \
                                and (Distance(check_agent.goal, agent.current_node) < Distance(check_agent.goal,
                                                                                               check_agent.current_node)):
                            print("Swapping Targets")
                            temp_goal = agent.goal
                            agent.goal = check_agent.goal
                            agent.path = agent.ASTAR(agent.current_node, agent.goal)
                            check_agent.path = check_agent.ASTAR(check_agent.current_node, temp_goal)
                            check_agent.goal = temp_goal
                            num_bad_conditions += 1

                    # ***** CHECK FOR COLLISIONS
                    # is there someone in the next node
                    if len(check_agent.path) > 0 and (check_agent.path[0].pos == agent.current_pos):
                        print("Someone is in the next node")

                        # if they intend to move, go ahead
                        # DON'T NEED TO MODIFY ANYTHING
                        # if they are paused due to inactivity, swap targets with them, you become inactive
                        if (agents_that_move[outer_agent_moving_index] == 0) and (len(agent.path) == 0):
                            print("Other agent inactive, swapping targets with them")
                            agent.goal = check_agent.goal
                            agent.ASTAR(agent.current_node, check_agent.goal)
                            check_agent.goal = check_agent.current_node
                            agents_that_move[outer_agent_moving_index] = 1

                            check_agent.path = []
                            agents_that_move[moving_index] = 0

                            num_bad_conditions += 1

                        # if they are paused for one turn, you pause too
                        elif (agents_that_move[outer_agent_moving_index] == 0) and (len(agent.path) > 0):
                            print("Agent is pausing, pausing this agent too")
                            agents_that_move[moving_index] = 0

                            num_bad_conditions += 1

                    # is there going to be a collision where they move into the same spot
                    if (agents_that_move[outer_agent_moving_index] == 1) and (len(agent.path) > 0) and (
                        len(check_agent.path) > 0):
                        if (agent.path[0] == check_agent.path[0]):
                            print("collision imminent")
                            num_bad_conditions += 1
                            agents_that_move[outer_agent_moving_index] = 0


                moving_index += 1
            outer_agent_moving_index += 1

        # if current solution looks good, finish loop
        if (num_bad_conditions == 0):
            ready_to_move = True

    print("AGENTS THAT MOVE", agents_that_move)

    # Move
    for cur_agent_index in range(len(agents)):
        if (agents_that_move[cur_agent_index] == 1):  # if agent is supposed to move this cycle
            print("PATH")
            for i in agents[cur_agent_index].path:
                print("<", i.pos, "> ", end='')
            print("")
            print("Moving agent", cur_agent_index)
            agents[cur_agent_index].move(agents[cur_agent_index].path)


# PPSOCycle()
# agents: list of instantiated agents with pre-populated current positions
# Completes one cycle of the Physically-embedded Particle Swarm Optimization Algorithm
# DESC: This algorithm iterates through solutions until optimal solution is met
# Optimal Solution Descriptions:
# No Target Sharing
# No other agent is closer to any given agent's target, unless there is no better target choice
# No next-move collisions between agents
def PPSOCycle(agents):
    ready_to_move = False
    report = []
    agents_that_move = [1] * len(agents)

    # Check for agents completed with their paths,
    # ensures every agent has a path if there are enough undiscovered locations
    for agent_index in range(len(agents)):
        if ((len(agents[agent_index].path) == 0) or (agents[agent_index].goal == agents[agent_index].current_node)):
            agents[agent_index].path = agents[agent_index].discover(agents[agent_index].current_node)
            print(agents[agent_index].path)

            if agents[agent_index].path == False:
                # nothing in agent's queue, grab from large pool

                if len(agents[agent_index].maze.undiscovered) > 0:
                    agents[agent_index].undiscovered.put(agents[agent_index].maze.undiscovered[0])
                    agents[agent_index].path = agents[agent_index].discover(agents[agent_index].current_node)
                    print(agents[agent_index].path)

                else:
                    # deactivate agent, nowhere for it to go
                    agents[agent_index].path = []
                    agents[agent_index].goal = agents[agent_index].current_node
                    print("Deactivating agent", agent_index)
                    agents_that_move[agent_index] = 0
    first_run = True
    # Conditional loop, loops until best solution for all agents is found
    while (ready_to_move == False):
        num_bad_conditions = 0  # number of issues with the next cycle to resolve
        outer_agent_moving_index = 0
        for agent in agents:
            moving_index = 0
            for check_agent in agents:

                # only look at agent if it is active and is not paused and not itself
                if (agent != check_agent) and (len(check_agent.path) > 0) and (agents_that_move[moving_index] == 1):

                    # ***** CHECK FOR TARGET CHANGE IF BOTH AGENTS ARE ACTIVE
                    if len(agent.path) > 0:

                        # check for shared targets
                        if (agent.goal == check_agent.goal):
                            print("Duplicate targets!")
                            if first_run is True:
                                report.append(("DUPLICATE_TARGETS", agent.goal.pos))
                            # find the furthest of the two agents and tell it to rediscover
                            if (len(agent.path) > len(check_agent.path)):
                                print("Path length case 1")
                                agent.path = agent.discover(agent.current_node)
                                if agent.path == False:
                                    # nothing in agent's queue, grab from large pool

                                    if len(agent.maze.undiscovered) > 0:
                                        print("Assigning new path to agent")
                                        agent.undiscovered.put(agent.maze.undiscovered[0])
                                        agent.path = agent.discover(agent.current_node)

                                    else:
                                        # deactivate agent, nowhere for it to go
                                        agent.path = []
                                        agent.goal = agent.current_node
                                        print("Deactivating agent", outer_agent_moving_index)
                                        agents_that_move[outer_agent_moving_index] = 0
                            else:
                                print("Path length case 2")
                                check_agent.path = check_agent.discover(check_agent.current_node)
                                if check_agent.path == False:
                                    # nothing in agent's queue, grab from large pool

                                    if len(check_agent.maze.undiscovered) > 0:
                                        print("Assigning new path to agent")
                                        check_agent.undiscovered.put(check_agent.maze.undiscovered[0])
                                        check_agent.path = check_agent.discover(check_agent.current_node)

                                    else:
                                        # deactivate agent, nowhere for it to go
                                        check_agent.path = []
                                        check_agent.goal = check_agent.current_node
                                        print("Deactivating agent", moving_index)
                                        agents_that_move[moving_index] = 0

                            num_bad_conditions += 1

                        # check for target swapping, if two agents are closer to eachothers goals than their own
                        if (Distance(agent.goal, check_agent.current_node) < Distance(agent.goal, agent.current_node)) \
                                and (Distance(check_agent.goal, agent.current_node) < Distance(check_agent.goal, check_agent.current_node)):
                            print("Swapping Targets")
                            if first_run is True:
                                report.append(("SWAPPING_TARGETS", agent.goal.pos, check_agent.goal.pos))
                            temp_goal = agent.goal
                            agent.goal = check_agent.goal
                            agent.path = agent.ASTAR(agent.current_node, agent.goal)
                            check_agent.path = check_agent.ASTAR(check_agent.current_node, temp_goal)
                            check_agent.goal = temp_goal
                            num_bad_conditions += 1

                    #***** CHECK FOR COLLISIONS
                    # is there someone in the next node
                    if len(check_agent.path) > 0 and (check_agent.path[0].pos == agent.current_pos):
                        print("Someone is in the next node")

                        # if they intend to move, go ahead
                            # DON'T NEED TO MODIFY ANYTHING
                        # if they are paused due to inactivity, swap targets with them, you become inactive
                        if (agents_that_move[outer_agent_moving_index] == 0) and (len(agent.path) == 0):
                            print("Other agent inactive, swapping targets with them")
                            if first_run is True:
                                report.append(("INACTIVE_AGENT_IN_NEXT_NODE", agent.current_pos))
                            agent.goal = check_agent.goal
                            agent.ASTAR(agent.current_node, check_agent.goal)
                            check_agent.goal = check_agent.current_node
                            agents_that_move[outer_agent_moving_index] = 1

                            check_agent.path = []
                            agents_that_move[moving_index] = 0

                            num_bad_conditions += 1

                        # if they are paused for one turn, you pause too
                        elif (agents_that_move[outer_agent_moving_index] == 0) and (len(agent.path) > 0):
                            print("Agent is pausing, pausing this agent too")
                            if first_run is True:
                                report.append(("PAUSED_AGENT_IN_NEXT_NODE", agent.current_pos))
                            agents_that_move[moving_index] = 0

                            num_bad_conditions += 1

                    # is there going to be a collision where they move into the same spot
                    if (agents_that_move[outer_agent_moving_index] == 1) and (len(agent.path) > 0) and (len(check_agent.path) > 0):
                        if(agent.path[0] == check_agent.path[0]):
                            print("collision imminent")
                            if first_run is True:
                                report.append(("COLLISION_EMMINENT_PAUSING_AGENT", agent.path[0].pos))
                            num_bad_conditions += 1
                            agents_that_move[outer_agent_moving_index] = 0



                moving_index += 1
            outer_agent_moving_index += 1

        print("num_bad_conditions: ", num_bad_conditions)

        # save first count of bad conditions for return
        if first_run is True:
            first_run = False

        # if current solution looks good, finish loop
        if (num_bad_conditions == 0):
            ready_to_move = True

    print("AGENTS THAT MOVE", agents_that_move)

    # Move
    for cur_agent_index in range(len(agents)):
        if (agents_that_move[cur_agent_index] == 1): # if agent is supposed to move this cycle
            print("Moving agent", cur_agent_index)
            agents[cur_agent_index].move(agents[cur_agent_index].path)

    return report
