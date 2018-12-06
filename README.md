Project: CMSC 471 Final Project
Project Title: Applying Path-Finding Techniques and Swarm Technologies to Package Delivery
Team Number: 3
Team Name: Number 3
Team Members: Alex Miu, Josh McCarter, Itay Tamary, Jack Wang
School: University of Maryland, Baltimore County
Due: December 5, 2018

This file is the README for our final AI project.
For detailed information about our project, read our paper!

Usage Instructions:
> python Driver.py maze_file_path max_agents PPSO
> python Driver.py maze_file_path max_agents PPSO debug

> python UI_Driver.py maze_file_path max_agents PPSO
> python UI_Driver.py maze_file_path max_agents PPSO debug

Note: Output files placed in same folder as Maze.
Note: Placing 'debug' at the end of the command will enable debug output.
Note: Some mazes (particularly large ones) take a while to run. They are still processing though.

File Layout:
- CMSC_471_Team3_Final_Paper.pdf:  Final Report
- Agent.py:  Agent class, contains A* pathfinding algorithm
- Maze.py:  Maze class, reads in maze from file
- Node.py:  Node class, basic struct for individual node of a graph
- UI.py:  Contains code for user interface
- UI_Driver.py:  User interface Driver
- Driver.py:  Full-test driver
- Swarm.py:  Contains swarm algorithm functions
- README.txt:  This file :)
- Swarm_Tests
    |
    |- Various Swarm Test Files
- image
    |
    |- Various UI image files
- Maze_Generation
    |
    |- MazeGenerator.js:  File requires Node.js to run. Randomly generates maze files of given size
    |- MazeVisualizer.html:  Used to view randomly generated maze files
    |- Mazes
        |
        |- largemazes
            |- various large mazes
        |- mediummazes
            |- various medium mazes
        |- smallmazes
            |- various small mazes
        |- tinymazes
            |- various tiny mazes
    |
    |- Testing
        |
        |- compute_stats.py:  Used for image generation
        |- gather_stats.py:  Runs a whole bunch of the tests
        |- AgentvsCycle.png
        |- AvgFrequencyOfError.png
        |- Figure1.png
        |- Proportion_XXXXX.png
        |- MazeCSVs
            |- various Driver.py output files