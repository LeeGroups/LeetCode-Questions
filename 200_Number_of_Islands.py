def numIslands(grid):
    stack = []
    seen = set()
    component = 0
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if (i,j) not in seen:
                seen.add((i,j))
                if grid[i][j] == "1":
                    stack.append((i,j))
                    while stack:
                        u,v = stack.pop()
                        seen.add((u,v))
                        if grid[u][v] == "1":
                            if u < n-1 and (u+1,v) not in seen:
                                stack.append((u+1,v))
                            if u > 0 and (u-1,v) not in seen:                                
                                stack.append((u-1,v))
                            if v < m-1 and (u,v+1) not in seen:
                                stack.append((u,v+1))
                            if v > 0 and (u,v-1) not in seen:                                
                                stack.append((u,v-1))
                    component += 1
    return component

# Test Cases

# Expect 1
print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

# Expect 3
print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

# Expect 1
print(numIslands(
    [["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]]))