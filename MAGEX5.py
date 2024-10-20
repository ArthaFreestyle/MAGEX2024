from collections import deque

def test(n, grid):
    if grid[0][0] == 'X' or grid[n-1][n-1] == 'X':
        return False
    
    directions = [(0, 1), (1, 0)]
    
    queue = deque([(0, 0)])
    
    visited = set()
    visited.add((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        if x == n-1 and y == n-1:
            return True
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == '.' and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y))
    
    return False

n = int(input())
grid = [input().strip() for _ in range(n)]

print(test(n,grid))