#file to automate test cases
from random import randint
from Driver import main

#get all the file names
tiny_file_names = ["Maze_Generation\Mazes"+"\\"+"tinymazes"+"\\"+"tinymaze1600_"+str(i)+".txt" for i in range(1,15001)]

NUM_AGENTS = 64
SWARM_ALGO = "PPSO"

#take 32 random mazes from each set

maze_files = []

#select the sample
for i in range(32):
    t_file = tiny_file_names[randint(0,14999)]
    maze_files.append(t_file)
   
#generate strings to send to main
input_lines = ["Driver "+file_name+" "+str(NUM_AGENTS)+" "+SWARM_ALGO for file_name in maze_files]
print(input_lines)
input_lines = [input_line.split() for input_line in input_lines]

#run for all
for input_line in input_lines:
    main(input_line)