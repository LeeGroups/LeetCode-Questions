import collections

def largestIsland(grid):
    boundaries = collections.defaultdict(set)
    height = len(grid)
    width = len(grid[0])
    stack = []
    seen = set()
    component_num = 0
    component_sizes = []
    for i in range(height):
        for j in range(width):
            if (i,j) not in seen:
                if grid[i][j] == 0:
                    seen.add((i,j))
                else:
                    stack.append((i,j))
                    component_size = 0
                    while stack:
                        x, y = stack.pop()
                        seen.add((x,y))
                        if grid[x][y] == 0:
                            boundaries[(x,y)].add(component_num)
                        else:
                            component_size += 1
                            if x > 0:
                                if (x-1,y) not in seen or grid[x-1][y] == 0:
                                    seen.add((x-1,y))
                                    stack.append((x-1,y))
                            if x < height-1:
                                if (x+1,y) not in seen or grid[x+1][y] == 0:
                                    seen.add((x+1,y))
                                    stack.append((x+1,y))
                            if y > 0:
                                if (x,y-1) not in seen or grid[x][y-1] == 0:
                                    seen.add((x,y-1))
                                    stack.append((x,y-1))
                            if y < width-1:
                                if (x,y+1) not in seen or grid[x][y+1] == 0:
                                    seen.add((x,y+1))
                                    stack.append((x,y+1))
                    component_sizes.append(component_size)
                    component_num += 1
    largest = 0    
    if boundaries:
        for elem in boundaries:
            size = 1
            for i in boundaries[elem]:
                size += component_sizes[i]
                largest = max(largest,size)
    else:
        if grid[0][0] == 0:
            largest = 1
        else:
            largest = height * width
    return largest

# faster than 82%