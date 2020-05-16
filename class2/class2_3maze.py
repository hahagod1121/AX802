# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:02:59 2020

@author: Jason
"""

maze = [[1,1,1,1,1,1,1,1,1,1],
        [1,0,1,1,1,1,1,1,1,1],
        [1,0,1,1,1,0,0,1,1,1],
        [1,0,1,0,0,0,1,1,1,1],
        [1,0,1,0,1,0,0,1,1,1],
        [1,0,0,0,1,1,0,1,1,1],
        [1,1,1,1,1,0,0,0,1,1],
        [1,1,1,1,1,0,1,1,1,1],
        [1,1,1,1,1,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]

#---------------------------------------#

visited = [[0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],]


start = [1,1]
end = [8,8]

pathstack = [(start[0],start[1])]

def run(y,x):
    if [x,y] == end:
        print("was at end")
        print(pathstack)
    if maze[y][x+1] == 0 and visited[y][x+1] == 0:
        visited[y][x+1] = 1
        pathstack.append([y,x+1])
        run(y,x+1)
        pathstack.pop()
    if maze[y][x-1] == 0 and visited[y][x-1] == 0:
        visited[y][x-1] = 1
        pathstack.append([y,x-1])
        run(y,x-1)
        pathstack.pop()
    if maze[y+1][x] == 0 and visited[y+1][x] == 0:
        visited[y+1][x] = 1
        pathstack.append([y+1,x])
        run(y+1,x)
        pathstack.pop()
    if maze[y-1][x] == 0 and visited[y-1][x] == 0:
        visited[y-1][x] = 1
        pathstack.append([y-1,x])
        run(y-1,x)
        pathstack.pop()

run(start[0],start[1])

