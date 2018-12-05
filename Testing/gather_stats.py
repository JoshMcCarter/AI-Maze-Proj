#file to automate test cases
from random import randint
from Driver import main

large_file_names = ["Maze_Generation\Mazes"+"\\"+"largemazes"+"\\"+"largemaze800000_"+str(i)+".txt" for i in range(1,101)]
medium_file_names = ["Maze_Generation\Mazes"+"\\"+"mediummazes400000"+"\\"+"largemaze400000_"+str(i)+".txt" for i in range(1,101)]
small_file_names = ["Maze_Generation\Mazes"+"\\"+"smallmazes"+"\\"+"smallermaze100000_"+str(i)+".txt" for i in range(1,211)]
tiny_file_names = ["Maze_Generation\Mazes"+"\\"+"tinymazes"+"\\"+"tinymaze1600_"+str(i)+".txt" for i in range(1,15001)]

NUM_AGENTS = 8
SWARM_ALGO = "PPSO"

#take 16 random mazes from each set

maze_files = []

#for i in range(32):
t_file = tiny_file_names[randint(0,14999)]
maze_files.append(t_file)
"""for i in range(4):
    s_file = small_file_names[randint(0,209)]
    maze_files.append(s_file)
for i in range(2):
    m_file = medium_file_names[randint(0,99)]
    maze_files.append(m_file)
for i in range(1):
    l_file = large_file_names[randint(0,99)]
    maze_files.append(l_file)"""



    
input_lines = [file_name+" "+str(NUM_AGENTS)+" "+SWARM_ALGO for file_name in maze_files]
print(input_lines)
input_lines = [input_line.split() for input_line in input_lines]

for input_line in input_lines:
    main(input_line)