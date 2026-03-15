import heapq
from collections import deque

GOAL_STATE = ((1,2,3),
              (4,5,6),
              (7,8,9))

MOVES = [(-1,0),(1,0),(0,-1),(0,1)]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j
            
def misplaced_tiles(state):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                cnt+=1
    return cnt                        

def manhattan_distance(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x = (val-1)//3
                y = (val-1)%3
                dist += abs(i-x) + dist(j-y)
    return dist            
    
def get_neighbours(state):
    x,y = find_zero(state)
    neighbours = []
    for dx,dy in MOVES:
        nx,ny = x + dx,y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [list(r) for r in state]
            new[nx][ny] , new[x][y] = new[x][y] , new[nx][ny]
            neighbours.append(tuple(tuple(r) for r in new))
    return neighbours        
                
def a_star(start,heuristic):
    pq = []
    heapq.heappush(pq,(start,heuristic(start),))
                    