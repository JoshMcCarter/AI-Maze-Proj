from tkinter import *
from Swarm import PPSOCycle

class UserInterface:
    def __init__(self, maze, agents):
        self.width = 500
        self.root = Tk()
        self.root.title("Main Map View")
        self.num_agents = 0
        for agent in agents:
            self.num_agents += 1
        self.agents_view = [0 for x in range(self.num_agents+10)]
        for i in range(0, self.num_agents):
            self.agents_view[i] = Toplevel()
            self.agents_view[i].title("Agent" + str(i+1))

        self.left_frame = Frame(self.root)
        self.right_frame = Frame(self.root)
        self.left_frame.pack(side=LEFT)
        self.right_frame.pack(side=RIGHT)

        self.one_step_flag = 0
        self.start_flag = False
        self.pause_flag = False


        def one_step():
            print("one step")
            PPSOCycle(agents)
            self.update(maze, agents)
            self.one_step_flag += 1
            self.pause_flag = False
            self.start_flag = False

        def start():
            print("start")
            self.start_flag = True
            self.pause_flag = False
            self.one_step_flag = 0
            while self.start_flag:
                PPSOCycle(agents)
                self.update(maze, agents)

        def pause():
            print("pause")
            self.pause_flag = True
            self.start_flag = False
            self.one_step_flag = 0


        self.button_one_step = Button(self.right_frame, text="One Step", fg="blue", command=one_step)
        self.button_start = Button(self.right_frame, text="Start", fg="blue", command=start)
        self.button_pause = Button(self.right_frame, text="Pause", fg="blue", command=pause)

        self.photo_cloud = PhotoImage(file="image/cloud.png")
        self.photo_d = PhotoImage(file="image/d.png")
        self.photo_dl = PhotoImage(file="image/dl.png")
        self.photo_dlr = PhotoImage(file="image/dlr.png")
        self.photo_dr = PhotoImage(file="image/dr.png")
        self.photo_l = PhotoImage(file="image/l.png")
        self.photo_lr = PhotoImage(file="image/lr.png")
        self.photo_r = PhotoImage(file="image/r.png")
        self.photo_u = PhotoImage(file="image/u.png")
        self.photo_ud = PhotoImage(file="image/ud.png")
        self.photo_udl = PhotoImage(file="image/udl.png")
        self.photo_udlr = PhotoImage(file="image/udlr.png")
        self.photo_udr = PhotoImage(file="image/udr.png")
        self.photo_ul = PhotoImage(file="image/ul.png")
        self.photo_ulr = PhotoImage(file="image/ulr.png")
        self.photo_ur = PhotoImage(file="image/ur.png")
        self.photo_agent = PhotoImage(file="image/agent.png")
        self.photo_empty = PhotoImage(file="image/empty.png")

        # get min and max x,y
        nodes = maze.nodes
        self.minx = 0
        self.maxx = 0
        self.miny = 0
        self.maxy = 0
        for node in nodes:
            if self.minx > node.pos[0]:
                self.minx = node.pos[0]
            if self.maxx < node.pos[0]:
                self.maxx = node.pos[0]
            if self.miny > node.pos[1]:
                self.miny = node.pos[1]
            if self.maxy < node.pos[1]:
                self.maxy = node.pos[1]
        self.labels = [[0 for x in range(self.maxx-self.minx+100)] for y in range(self.maxy-self.miny+100)]
        self.size = 0
        if self.maxx - self.minx - (self.maxy - self.miny) > 0:
            self.size = self.width/(self.maxx - self.minx)
        else:
            self.size = self.width/(self.maxy - self.miny)

        if self.size > 50:
            self.size = 50

        # show default maze
        for i in range(0, self.maxx - self.minx + 1):
            for j in range(0, self.maxy - self.miny + 1):
                self.labels[i][j] = \
                    Label(self.left_frame,image=self.photo_empty,bg="black", width=self.size, height=self.size)
                self.labels[i][j].grid(row=j, column=i)

        for node in nodes:
            i = node.pos[0]
            j = node.pos[1]
            self.labels[i - self.minx][j - self.miny] = \
                Label(self.left_frame, image=self.photo_empty, bg="gray", width=self.size, height=self.size)
            self.labels[i - self.minx][j - self.miny].grid(row=j - self.miny, column=i - self.minx)

        for agent in agents:
            i = agent.current_pos[0]
            j = agent.current_pos[1]
            self.labels[i - self.minx][j - self.miny] = \
                Label(self.left_frame, image=self.photo_empty, bg="red", width=self.size, height=self.size)
            self.labels[i - self.minx][j - self.miny].grid(row=j - self.miny, column=i - self.minx)

        self.agents_labels = [[[0 for x in range(5)] for y in range(5)] for z in range(self.num_agents)]
        for k in range(0, self.num_agents):
            for i in range(0, 5):
                for j in range(0, 5):
                    self.agents_labels[k][i][j] = \
                        Label(self.agents_view[k], image=self.photo_cloud, width=50, height=50)
                    self.agents_labels[k][i][j].grid(row=j, column=i)
            self.agents_labels[k][i][j] = \
                Label(self.agents_view[k], image=self.photo_agent, width=50, height=50)
            self.agents_labels[k][i][j].grid(row=2, column=2)
            self.agents_view[k].update()
        self.button_one_step.pack(fill=X)
        self.button_start.pack(fill=X)
        self.button_pause.pack(fill=X)
        self.root.mainloop()

    def update(self, maze, agents):

        nodes = maze.nodes

        for node in nodes:
            if node.discovered:
                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                    Label(self.left_frame, image=self.photo_empty, bg="green", width=self.size, height=self.size)
                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny]. \
                    grid(row=node.pos[1] - self.miny, column=node.pos[0] - self.minx)
        for agent in agents:
            i = agent.current_pos[0]
            j = agent.current_pos[1]
            self.labels[i][j] = \
                Label(self.left_frame, image=self.photo_empty, bg="red", width=self.size, height=self.size)
            self.labels[i][j].grid(row=j, column=i)
        self.root.update()

        #update for agents
        for k in range(0, self.num_agents):
            for i in range(0, 5):
                for j in range(0, 5):
                    x = agents[k].current_pos[0]
                    y = agents[k].current_pos[1]
                    x = x + i - 2
                    y = y + j - 2
                    if x < 0:
                        self.agents_labels[k][i][j] = \
                            Label(self.agents_view[k], image=self.photo_cloud, width=50, height=50)
                        self.agents_labels[k][i][j].grid(row=j, column=i)
                        continue
                    if x > self.maxx-self.minx:
                        self.agents_labels[k][i][j] = \
                            Label(self.agents_view[k], image=self.photo_cloud, width=50, height=50)
                        self.agents_labels[k][i][j].grid(row=j, column=i)
                        continue
                    if y < 0:
                        self.agents_labels[k][i][j] = \
                            Label(self.agents_view[k], image=self.photo_cloud, width=50, height=50)
                        self.agents_labels[k][i][j].grid(row=j, column=i)
                        continue
                    if y > self.maxy-self.miny:
                        self.agents_labels[k][i][j] = \
                            Label(self.agents_view[k], image=self.photo_cloud, width=50, height=50)
                        self.agents_labels[k][i][j].grid(row=j, column=i)
                        continue
                    self.agents_labels[k][i][j] = \
                        Label(self.agents_view[k], image=self.photo_cloud, width=50, height=50)
                    self.agents_labels[k][i][j].grid(row=j, column=i)

                    for node in nodes:
                        if node.discovered:
                            if node.pos[0] == x and node.pos[1] == y:
                                if node.up:
                                    if node.down:
                                        if node.left:
                                            if node.right:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_udlr, width=50,
                                                          height=50)
                                            else:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_udl, width=50,
                                                          height=50)
                                        else:
                                            if node.right:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_udr, width=50,
                                                          height=50)
                                            else:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_ud, width=50, height=50)
                                    else:
                                        if node.left:
                                            if node.right:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_ulr, width=50,
                                                          height=50)
                                            else:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_ul, width=50, height=50)
                                        else:
                                            if node.right:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_ur, width=50, height=50)
                                            else:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_u, width=50, height=50)
                                else:
                                    if node.down:
                                        if node.left:
                                            if node.right:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_dlr, width=50,
                                                          height=50)
                                            else:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_dl, width=50, height=50)
                                        else:
                                            if node.right:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_dr, width=50, height=50)
                                            else:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_d, width=50, height=50)
                                    else:
                                        if node.left:
                                            if node.right:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_lr, width=50, height=50)
                                            else:
                                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                                    Label(self.agents_view[k], image=self.photo_l, width=50, height=50)
                                        else:
                                            if node.right:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_r, width=50, height=50)
                                            else:
                                                self.agents_labels[k][i][j] = \
                                                    Label(self.agents_view[k], image=self.photo_cloud, width=50,
                                                          height=50)
                            self.agents_labels[k][i][j].grid(row=j, column=i)
                    if i == 2 and j ==2:
                        self.agents_labels[k][i][j] = \
                            Label(self.agents_view[k], image=self.photo_agent, width=50, height=50)
                        self.agents_labels[k][i][j].grid(row=j, column=i)
            self.agents_view[k].update()
