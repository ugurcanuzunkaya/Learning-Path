from pyamaze import *
import tkinter as tk
from tkinter import messagebox
from collections import deque


def DFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfs_path = {}
    d_search = []
    while len(frontier) > 0:
        current_cell = frontier.pop()
        d_search.append(current_cell)
        if current_cell == m._goal:
            break
        poss = 0
        for d in "ESNW":
            if m.maze_map[current_cell][d] == True:
                if d == "E":
                    child_cell = (current_cell[0], current_cell[1] + 1)
                elif d == "W":
                    child_cell = (current_cell[0], current_cell[1] - 1)
                elif d == "S":
                    child_cell = (current_cell[0] + 1, current_cell[1])
                elif d == "N":
                    child_cell = (current_cell[0] - 1, current_cell[1])
                if child_cell in explored:
                    continue
                poss += 1
                explored.append(child_cell)
                frontier.append(child_cell)
                dfs_path[child_cell] = current_cell
        if poss > 1:
            m.markCells.append(current_cell)
    forward_path = {}
    cell = m._goal
    while cell != start:
        forward_path[dfs_path[cell]] = cell
        cell = dfs_path[cell]
    return d_search, dfs_path, forward_path


def BFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    explored = [start]
    frontier = deque()
    frontier.append(start)
    bfs_path = {}
    b_search = []
    while len(frontier) > 0:
        current_cell = frontier.popleft()
        b_search.append(current_cell)
        if current_cell == m._goal:
            break
        for d in "ESNW":
            if m.maze_map[current_cell][d] == True:
                if d == "E":
                    child_cell = (current_cell[0], current_cell[1] + 1)
                elif d == "W":
                    child_cell = (current_cell[0], current_cell[1] - 1)
                elif d == "S":
                    child_cell = (current_cell[0] + 1, current_cell[1])
                elif d == "N":
                    child_cell = (current_cell[0] - 1, current_cell[1])
                if child_cell in explored:
                    continue
                explored.append(child_cell)
                frontier.append(child_cell)
                bfs_path[child_cell] = current_cell
                b_search.append(child_cell)
    forward_path = {}
    cell = m._goal
    while cell != start:
        forward_path[bfs_path[cell]] = cell
        cell = bfs_path[cell]
    return b_search, bfs_path, forward_path


def dijikstra(m, *h, start=None):
    if start is None:
        start = (m.rows, m.cols)

    hurdles = [(i.position, i.cost) for i in h]
    unvisited = {n: float('inf') for n in m.grid}
    unvisited[start] = 0
    visited = {}
    rev_path = {}
    while unvisited:
        current_cell = min(unvisited, key=unvisited.get)
        visited[current_cell] = unvisited[current_cell]
        if current_cell == m._goal:
            break
        for d in "EWNS":
            if m.maze_map[current_cell][d] == True:
                if d == "E":
                    child_cell = (current_cell[0], current_cell[1] + 1)
                elif d == "W":
                    child_cell = (current_cell[0], current_cell[1] - 1)
                elif d == "S":
                    child_cell = (current_cell[0] + 1, current_cell[1])
                elif d == "N":
                    child_cell = (current_cell[0] - 1, current_cell[1])
                if child_cell in visited:
                    continue
                temp_dist = unvisited[current_cell] + 1
                for hurdle in hurdles:
                    if hurdle[0] == current_cell:
                        temp_dist += hurdle[1]

                if temp_dist < unvisited[child_cell]:
                    unvisited[child_cell] = temp_dist
                    rev_path[child_cell] = current_cell
        unvisited.pop(current_cell)
    forward_path = {}
    cell = m._goal
    while cell != start:
        forward_path[rev_path[cell]] = cell
        cell = rev_path[cell]

    return forward_path, visited[m._goal]


def create_maze(height_maze, width_maze, width_path, hardness_maze, start_point_x, start_point_y, end_point_x,
                end_point_y, pattern_maze):
    m = maze(height_maze, width_maze)
    if 0 < end_point_x <= width_maze and 0 < end_point_y <= height_maze and 0 < start_point_x <= width_maze and 0 < start_point_y <= height_maze:
        if pattern_maze.lower() in ["v", "vertical"]:
            m.CreateMaze(x=end_point_x, y=end_point_y, loopPercent=50, pattern="v")
        elif pattern_maze.lower() in ["h", "horizontal"]:
            m.CreateMaze(x=end_point_x, y=end_point_y, loopPercent=50, pattern="h")
        else:
            tk.messagebox.showinfo("Error", "Pattern not found! Please try again.")
            return
        if hardness_maze.lower() in ["e", "easy"]:
            a = agent(m, x=start_point_x, y=start_point_y, footprints=True, shape="arrow", color=COLOR.green)
            p, l, v = DFS(m, (start_point_x, start_point_y))
            b = agent(m, x=start_point_x, y=start_point_y, footprints=True, shape="arrow", color=COLOR.cyan)
            o, k, n = BFS(m, (start_point_x, start_point_y))
            c = agent(m, x=start_point_x, y=start_point_y, footprints=True, shape="arrow", color=COLOR.blue)
            u, j = dijikstra(m, start=(start_point_x, start_point_y))
            m.tracePath({a: v, b: n, c: u})
        elif hardness_maze.lower() in ["m", "medium"]:
            a = agent(m, x=start_point_x, y=start_point_y, footprints=True, shape='arrow', color=COLOR.green)
            p, l, v = DFS(m, (start_point_x, start_point_y))
            b = agent(m, x=start_point_x, y=start_point_y, footprints=True, shape='arrow', color=COLOR.cyan)
            o, k, n = BFS(m, (start_point_x, start_point_y))
            m.tracePath({a: v, b: n})
        elif hardness_maze.lower() in ["h", "hard"]:
            a = agent(m, x=start_point_x, y=start_point_y, footprints=True, shape="arrow", color=COLOR.green)
            p, l, v = DFS(m, (start_point_x, start_point_y))
            m.tracePath({a: v})
        else:
            tk.messagebox.showinfo("Error", "Hardness not found! Please try again.")
            return
        m.run()
    else:
        tk.messagebox.showinfo("Error", "Start or end points is/are out of range! Please try again.")
        return


def creating_maze():
    q, w, e, r, t, y, s, d, f = int(entry1.get()), int(entry2.get()), int(entry3.get()), entry4.get(), \
                                int(entry5.get()), int(entry6.get()), int(entry7.get()), int(entry8.get()), entry9.get()
    window.destroy()
    create_maze(q, w, e, r, t, y, s, d, f)


window = tk.Tk()
window.title("Maze Generator Main Window")
window.geometry("500x500")

label1 = tk.Label(window, text="Height of Maze:")
label1.grid(column=0, row=0)
entry1 = tk.Entry(window)
entry1.grid(column=1, row=0)
label2 = tk.Label(window, text="Width of Maze:")
label2.grid(column=0, row=1)
entry2 = tk.Entry(window)
entry2.grid(column=1, row=1)
label3 = tk.Label(window, text="Width of Path:")
label3.grid(column=0, row=2)
entry3 = tk.Entry(window)
entry3.grid(column=1, row=2)
label4 = tk.Label(window, text="Hardness of Maze:")
label4.grid(column=0, row=3)
entry4 = tk.Entry(window)
entry4.grid(column=1, row=3)
label5 = tk.Label(window, text="Start Point X:")
label5.grid(column=0, row=4)
entry5 = tk.Entry(window)
entry5.grid(column=1, row=4)
label6 = tk.Label(window, text="Start Point Y:")
label6.grid(column=0, row=5)
entry6 = tk.Entry(window)
entry6.grid(column=1, row=5)
label7 = tk.Label(window, text="End Point X:")
label7.grid(column=0, row=6)
entry7 = tk.Entry(window)
entry7.grid(column=1, row=6)
label8 = tk.Label(window, text="End Point Y:")
label8.grid(column=0, row=7)
entry8 = tk.Entry(window)
entry8.grid(column=1, row=7)
label9 = tk.Label(window, text="Pattern of Maze:")
label9.grid(column=0, row=8)
entry9 = tk.Entry(window)
entry9.grid(column=1, row=8)
button1 = tk.Button(window, text="Create Maze", command=creating_maze)
button1.grid(column=0, row=9)
window.mainloop()
