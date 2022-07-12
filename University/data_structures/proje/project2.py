from pyamaze import *
import tkinter as tk
from tkinter import messagebox

"""height_maze = int(input("Enter the height of the maze: "))
width_maze = int(input("Enter the width of the maze: "))
width_path = int(input("Enter the width of the path: "))
hardness_maze = input("Enter the hardness of the maze: ")
start_point_x = int(input("Enter the x of start point of the maze: "))
start_point_y = int(input("Enter the y of start point of the maze: "))
end_point_x = int(input("Enter the x of end point of the maze: "))
end_point_y = int(input("Enter the y of end point of the maze: "))
pattern_maze = input("Enter the pattern of the maze (vertical(v) or horizontal(h)): ")
"""


def maze_gen_solve(height_maze, width_maze, width_path, hardness_maze, start_point_x, start_point_y, end_point_x,
                   end_point_y, pattern_maze):
    if hardness_maze.lower() == "easy":
        m = maze(height_maze, width_maze)
        if 0 < end_point_x <= width_maze and 0 < end_point_y <= height_maze and 0 < start_point_x <= width_maze \
                and 0 < start_point_y <= height_maze:
            if pattern_maze.lower() in ["v", "vertical"]:
                m.CreateMaze(x=end_point_x, y=end_point_y, loopPercent=0, pattern="v")
                a = agent(m, x=start_point_x, y=start_point_y, footprints=True)
                m.tracePath({a: m.path, b: m.path, c:m.path})
                m.run()
            elif pattern_maze.lower() in ["h", "horizontal"]:
                m.CreateMaze(end_point_x, end_point_y, loopPercent=0, pattern="h")
                a = agent(m, x=start_point_x, y=start_point_y, goal=(end_point_x, end_point_y), footprints=True)
                m.tracePath({a: m.path})
                m.run()
            else:
                tk.messagebox.showinfo("Error", "Pattern of the maze is not correct")
        else:
            tk.messagebox.showinfo("Error", "Invalid end point")

    elif hardness_maze.lower() == "medium":
        m = maze(height_maze, width_maze)
        if 0 < end_point_x <= width_maze and 0 < end_point_y <= height_maze and 0 < start_point_x <= width_maze \
                and 0 < start_point_y <= height_maze:
            if pattern_maze.lower() in ["v", "vertical"]:
                m.CreateMaze(x=end_point_x, y=end_point_y, loopPercent=0, pattern="v")
                a = agent(m, x=start_point_x, y=start_point_y, footprints=True)
                m.tracePath({a: m.path})
                m.run()
            elif pattern_maze.lower() in ["h", "horizontal"]:
                m.CreateMaze(end_point_x, end_point_y, loopPercent=0, pattern="h")
                a = agent(m, x=start_point_x, y=start_point_y, goal=(end_point_x, end_point_y), footprints=True)
                m.tracePath({a: m.path})
                m.run()
            else:
                tk.messagebox.showinfo("Error", "Invalid pattern")
        else:
            tk.messagebox.showinfo("Error", "Invalid points")

    elif hardness_maze.lower() == "hard":
        m = maze(height_maze, width_maze)
        if 0 < end_point_x <= width_maze and 0 < end_point_y <= height_maze and 0 < start_point_x <= width_maze \
                and 0 < start_point_y <= height_maze:
            if pattern_maze.lower() in ["v", "vertical"]:
                m.CreateMaze(x=end_point_x, y=end_point_y, loopPercent=0, pattern="v")
                a = agent(m, x=start_point_x, y=start_point_y, footprints=True)
                m.tracePath({a: m.path})
                m.run()
            elif pattern_maze.lower() in ["h", "horizontal"]:
                m.CreateMaze(end_point_x, end_point_y, loopPercent=0, pattern="h")
                a = agent(m, x=start_point_x, y=start_point_y, goal=(end_point_x, end_point_y), footprints=True)
                m.tracePath({a: m.path})
                m.run()
            else:
                tk.messagebox.showinfo("Invalid pattern", "Invalid pattern")
        else:
            tk.messagebox.showinfo("Error", "Invalid points")

    else:
        tk.messagebox.showinfo("Error", "Invalid hardness")


def createMaze():
    q, w, e, r, t, y, u, o, p = int(entry1.get()), int(entry2.get()), int(entry3.get()), entry4.get(), int(
        entry5.get()), int(entry6.get()), int(entry7.get()), int(entry8.get()), entry9.get()
    window.destroy()
    maze_gen_solve(q, w, e, r, t, y, u, o, p)


window = tk.Tk()
window.title("Pyamaze")
window.geometry("800x600")

label1 = tk.Label(window, text="Height of the maze: ")
label1.pack()
entry1 = tk.Entry()
entry1.pack()
label2 = tk.Label(window, text="Width of the maze: ")
label2.pack()
entry2 = tk.Entry()
entry2.pack()
label3 = tk.Label(window, text="Width of the path: ")
label3.pack()
entry3 = tk.Entry()
entry3.pack()
label4 = tk.Label(window, text="Hardness of the maze: ")
label4.pack()
entry4 = tk.Entry()
entry4.pack()
label5 = tk.Label(window, text="Start point of x of the maze: ")
label5.pack()
entry5 = tk.Entry()
entry5.pack()
label6 = tk.Label(window, text="Start point of y of the maze: ")
label6.pack()
entry6 = tk.Entry()
entry6.pack()
label7 = tk.Label(window, text="End point of x of the maze: ")
label7.pack()
entry7 = tk.Entry()
entry7.pack()
label8 = tk.Label(window, text="End point of y of the maze: ")
label8.pack()
entry8 = tk.Entry()
entry8.pack()
label9 = tk.Label(window, text="Pattern of the maze: ")
label9.pack()
entry9 = tk.Entry()
entry9.pack()
button1 = tk.Button(window, text="Create", command=createMaze)
button1.pack()

window.mainloop()

"""
colors is tkinter color list
theme= in CreateMaze
color= in agent
m.enableArrowKey(a)
m.enableWASD(a)
"""
"""
m = maze(height_maze, width_maze)
if 0 < end_point_x <= width_maze and 0 < end_point_y <= height_maze and 0 < start_point_x <= width_maze and 0 < start_point_y <= height_maze:
    if pattern_maze.lower() in ["v", "vertical"]:
        m.CreateMaze(x=end_point_x, y=end_point_y, loopPercent=0, pattern="v")
        a = agent(m, x=start_point_x, y=start_point_y, footprints=True)
        m.tracePath({a: m.path})
        m.run()
    elif pattern_maze.lower() in ["h", "horizontal"]:
        m.CreateMaze(end_point_x, end_point_y, loopPercent=0, pattern="h")
        a = agent(m, x=start_point_x, y=start_point_y, goal=(end_point_x, end_point_y), footprints=True)
        m.tracePath({a: m.path})
        m.run()
    else:
        print("Invalid pattern")
else:
    print("Invalid points")
"""
