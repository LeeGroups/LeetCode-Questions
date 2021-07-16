def isBipartite(graph):
    result = True
    A = {0: True}
    B = {}
    stack = graph[0]      
    def helper():
        nonlocal stack
        while stack:
            i = stack.pop(-1)
            in_A = i in A
            for j in range(len(graph[i])):
                if in_A:
                    if graph[i][j] in A:
                        return False
                    if graph[i][j] not in B:
                        stack.append(graph[i][j])
                        B[graph[i][j]] = True
                else:
                    if graph[i][j] in B:
                        return False
                    if graph[i][j] not in A:
                        stack.append(graph[i][j])
                        A[graph[i][j]] = True 
        for i in range(len(graph)):
            if i not in A and i not in B and graph[i] != []:
                stack = graph[i]
                return helper()
        return True
    return helper()

                
""" beats 71.5%"""

# sample inputs:

# Expect False
print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))

# Expect True
print(isBipartite([[1,3],[0,2],[1,3],[0,2]]))

# Expect True
print(isBipartite([[4],[],[4],[4],[0,2,3]]))

# Expect false
print(isBipartite([[4,1],[0,2],[1,3],[2,4],[3,0]]))

# Expect false
print(isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))

# Expect false
print(isBipartite([[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]
))