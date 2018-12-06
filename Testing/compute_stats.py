import matplotlib.pyplot as plt
import numpy as np
import csv
from random import randint
import re

START_PATH = "MazeCSVs\\tinymaze1600_"
END_PATH = "_OUTPUT.csv"
SAMPLE_NUMS = [107,1749,4462,4499,4649,4771,5649,5726,5827,5879,6153,6861,7422,8667,8926,8957,9563,10247,10534,11472,11476,11573,11841,11945,12305,12616,12681,12787,12863,14510,14883]
NUM_SAMPLES = len(SAMPLE_NUMS)
paths = [START_PATH+str(num)+END_PATH for num in SAMPLE_NUMS]

nodes_per_file = []
avg_collisions = []
cycles_per_agent = [] 
avg_cycles = []
random_case = 9

def get_agents_moved_per_cycle():
    list_of_agents_per_cycle = []
    path = paths[random_case]
    with open(path, newline='') as csvfile:
        for line in csvfile:
            info = line.split(",")
            if len(info) > 4 and int(info[0]) == 63:
                if info[5] == "\"AGENTS_THAT_MOVE_THIS_CYCLE\"":
                    num = info[6][1:3]
                    foo = re.sub('\"','',num)
                    list_of_agents_per_cycle.append(int(foo))
        csvfile.close()
            
    return list_of_agents_per_cycle

def get_frequencies_of_errors():
    all_freqs = []
    for path in paths:
        curr_file_freqs = {i:[0,0,0,0,0] for i in range(1,64)}
        with open(path, newline='') as csvfile:
            for line in csvfile:
                info = line.split(",")
                if len(info) > 4:
                    if info[5] == "\"SWAPPING_TARGETS\"":
                        curr_file_freqs[int(info[0])][0] += 1
                    elif info[5] == "\"INACTIVE_AGENT_IN_NEXT_NODE\"":
                        curr_file_freqs[int(info[0])][1] += 1
                    elif info[5] == "\"PAUSED_AGENT_IN_NEXT_NODE\"":
                        curr_file_freqs[int(info[0])][2] += 1
                    elif info[5] == "\"COLLISION_EMMINENT_PAUSING_AGENT\"":
                        curr_file_freqs[int(info[0])][3] += 1
                    elif info[5] == "\"DUPLICATE_TARGETS\"":
                        curr_file_freqs[int(info[0])][4] += 1
            csvfile.close()
        all_freqs.append(curr_file_freqs)
    return all_freqs

def calculate_average_freqs(frequencies):
    total_freqs = {i:[0,0,0,0,0] for i in range(1,64)}
    for i in range(len(frequencies)):
        for key in frequencies[i].keys():
            for j in range(5):
                total_freqs[key][j] += frequencies[i][key][j]
    
    for key in total_freqs.keys():
        for i in range(5):
            total_freqs[key][i] /= NUM_SAMPLES
            
    return total_freqs
    
def get_average_nodes_per_file():
    for path in paths:
        with open(path, newline='') as csvfile:
            for line in csvfile:
                info = line.split(",")
                nodes_per_file.append(int(info[2]))
                break
            csvfile.close()       
    return sum(nodes_per_file)/len(nodes_per_file)

def get_cylcles_per_agent():
    for path in paths:
        with open(path, newline='') as csvfile:
            agents_in_current = []
            for line in csvfile:
                info = line.split(",")
                if info[0] == "TOTAL_CYCLES":
                    num_cycles = info[1]
                    agents_in_current.append(int(num_cycles))
                    
            cycles_per_agent.append(agents_in_current)
            csvfile.close()

def compute_avg_cycles_per_agent():
    averages = [0 for i in range(63)]
    for i in range(len(cycles_per_agent)):
        for j in range(63):
            averages[j] += cycles_per_agent[i][j]
    averages = [averages[i]/NUM_SAMPLES for i in range(len(averages))]
    return averages
    

    
def get_reconstructs_per_agent():
    collisions = [0 for i in range(64)]
    error_lines = []
    for path in paths:
        with open(path, newline='') as csvfile:
            for line in csvfile:
                info = line.split(",")
                if len(info) > 4:
                    if info[5] != "\"AGENTS_THAT_MOVE_THIS_CYCLE\"":
                        error_lines.append(info)
            csvfile.close()
 
    for line in error_lines:
        collisions[int(line[0])] += 1    
    return [collisions[i]/NUM_SAMPLES for i in range(len(collisions))]
    
    
def make_graphs():
    get_cylcles_per_agent()
    avg_cycles = compute_avg_cycles_per_agent()
    avg_collisions = get_reconstructs_per_agent()
    input_cycles = np.array(avg_cycles)
    input_collisions = np.array(avg_collisions)
    
    """plt.plot([i for i in range(1,64)],avg_cycles,'ro')
    plt.suptitle('Number of Agents vs. Average Cycles')
    plt.xlabel('Number of Agents')
    plt.ylabel('Average Number of Cycles')
    plt.axis([0,64,0,3000])
    plt.show()
    
    plt.plot([i for i in range(1,65)],avg_collisions,'ro')
    plt.suptitle('Number of Agents vs. Average Collisions')
    plt.xlabel('Number of Agents')
    plt.ylabel('Average Number of Collisions')
    plt.axis([0,64,0,300])
    plt.show()
    
    freqs_per_file = get_frequencies_of_errors()
    avg_freqs = calculate_average_freqs(freqs_per_file)
    
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    
    #make tuples of each avg freq
    for i in range(1,len(avg_freqs.keys())):
        list1.append(avg_freqs[i][0])
        list2.append(avg_freqs[i][1])
        list3.append(avg_freqs[i][2])
        list4.append(avg_freqs[i][3])
        list5.append(avg_freqs[i][4])
    
    fig,ax = plt.subplots()
    n_agents = 62
    bar_width = 0.2
    opacity = 0.8
    index = np.arange(n_agents)
    rects1 = plt.bar(index,list1,bar_width,alpha=opacity,color='r',label='Swapping Targets',edgecolor="black")
    rects2 = plt.bar(index+bar_width,list2,bar_width,alpha=opacity,color='b',label='Inactive Agent in Next Node',edgecolor="black")
    rects3 = plt.bar(index+2*bar_width,list3,bar_width,alpha=opacity,color='g',label='Paused Agent in Next Node',edgecolor="black")
    rects4 = plt.bar(index+3*bar_width,list4,bar_width,alpha=opacity,color='y',label='Colission Emminent Pausing Agent',edgecolor="black")
    rects5 = plt.bar(index+4*bar_width,list5,bar_width,alpha=opacity,color='k',label='Duplicate Targets',edgecolor="black")
    
    ax.autoscale(tight=True)
    
    plt.suptitle('Average Frequency of Each Type of Conflict for a Number Of Agents on a Maze With Max 1600 Nodes')
    plt.xlabel('Number of Agents')
    plt.ylabel('Average Frequency of Conflict')
    plt.xticks(index+2.5*bar_width,(i for i in range(2,64)))
    plt.legend()
    plt.show()"""
    
    agents_moved_per_cycle = get_agents_moved_per_cycle()
    prop_of_agents_moved_per_cycle = [agents_moved_per_cycle[i]/63 for i in range(len(agents_moved_per_cycle))]
    
    plt.plot([i for i in range(1,len(agents_moved_per_cycle)+1)],prop_of_agents_moved_per_cycle,'.')
    plt.suptitle('Propotion of Agents Used per Cycle on Maze ' + str(SAMPLE_NUMS[random_case]) + " With 63 Agents")
    plt.xlabel('Cycle Number')
    plt.ylabel('Proportion of Agents Used')
    plt.axis([1,len(agents_moved_per_cycle),0,1.1])
    plt.show()
    
    
    
    
make_graphs()
    