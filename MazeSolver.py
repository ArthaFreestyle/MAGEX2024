import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

maze = [
    "# ###########",
    "#         # #",
    "# ####### # #",
    "# #       # #",
    "# # ####### #",
    "# #       # #",
    "# ######### #",
    "#           #",
    "########### #"
]

dir = [
    (-1, 0),  
    (0, 1),   
    (1, 0),  
    (0, -1)    
]

def walk(maze, wall, end, curr, seen, path, steps):
    x, y = curr["x"], curr["y"]

    if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
        return False
    if maze[y][x] == wall or seen[y][x]:
        return False
    if x == end["x"] and y == end["y"]:
        path.append((x, y))
        steps.append(list(path)) 
        return True

    seen[y][x] = True
    path.append((x, y))
    steps.append(list(path)) 

    for dx, dy in dir:
        if walk(maze, wall, end, {"x": x + dx, "y": y + dy}, seen, path, steps):
            return True

    path.pop()
    steps.append(list(path))
    return False

def solveMaze(maze, start, end):
    seen = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    path = []
    steps = []
    walk(maze, "#", end, start, seen, path, steps)
    return steps

def convert_maze_to_grid(maze):
    rows, cols = len(maze), len(maze[0])
    grid = np.zeros((rows, cols))
    for y in range(rows):
        for x in range(cols):
            if maze[y][x] == "#":
                grid[y][x] = 1
    return grid

start = {"x": 1, "y": 0}
end = {"x": 11, "y": 8}

steps = solveMaze(maze, start, end)

grid = convert_maze_to_grid(maze)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xticks([])
ax.set_yticks([])
ax.imshow(grid, cmap="gray_r")

scatter = ax.scatter([], [], color="red", s=50)

def update(frame):
    if frame < len(steps):
        scatter.set_offsets(steps[frame])
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=200, repeat=False)

plt.show()
