from tkinter import *


class UserInterface:
    def __init__(self, maze):
        self.root = Tk()
        self.root.title("Maze Breaker")

        self.left_frame = Frame(self.root)
        self.right_frame = Frame(self.root)
        self.left_frame.pack(side=LEFT)
        self.right_frame.pack(side=RIGHT)

        def one_step():
            print("one step")

        def start():
            print("start")

        def pause():
            print("pause")
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
        self.labels = [[0 for x in range(self.maxx-self.minx+1)] for y in range(self.maxy-self.miny+1)]
        # show default maze
        for i in (self.minx, self.maxx):
            for j in (self.minx, self.maxy):
                self.labels[i-self.minx][j-self.miny] = \
                    Label(self.left_frame, image=self.photo_cloud, width=50, height=50)
                self.labels[i - self.minx][j - self.miny].grid(row=i-self.minx, column=j-self.miny)

        self.button_one_step.pack(fill=X)
        self.button_start.pack(fill=X)
        self.button_pause.pack(fill=X)
        self.root.mainloop()

    def update(self, maze):

        nodes = maze.nodes

        for node in nodes:
            if node.discovered:
                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny].pack_forgot()
                if node.up:
                    if node.down:
                        if node.left:
                            if node.right:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_udlr, width=50, height=50)
                            else:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_udl, width=50, height=50)
                        else:
                            if node.right:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_udr, width=50, height=50)
                            else:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_ud, width=50, height=50)
                    else:
                        if node.left:
                            if node.right:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_ulr, width=50, height=50)
                            else:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_ul, width=50, height=50)
                        else:
                            if node.right:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_ur, width=50, height=50)
                            else:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_u, width=50, height=50)
                else:
                    if node.down:
                        if node.left:
                            if node.right:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_dlr, width=50, height=50)
                            else:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_dl, width=50, height=50)
                        else:
                            if node.right:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_dr, width=50, height=50)
                            else:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_d, width=50, height=50)
                    else:
                        if node.left:
                            if node.right:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_lr, width=50, height=50)
                            else:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_l, width=50, height=50)
                        else:
                            if node.right:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_r, width=50, height=50)
                            else:
                                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny] = \
                                    Label(self.left_frame, image=self.photo_cloud, width=50, height=50)
                self.labels[node.pos[0] - self.minx][node.pos[1] - self.miny].\
                    grid(row=node.pos[0] - self.minx, column=node.pos[1] - self.miny)
        self.root.update()
