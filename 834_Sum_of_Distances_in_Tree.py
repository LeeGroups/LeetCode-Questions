import collections

def sumOfDistancesInTree(n, edges):
    adjacency = collections.defaultdict(set)
    for edge in edges:
        adjacency[edge[0]].add(edge[1])
        adjacency[edge[1]].add(edge[0])
        
    count = [1 for _ in range(n)]
    dist = [0 for _ in range(n)]
    
    def counter(root, parent):
        for node in adjacency[root]:
            if node != parent:
                counter(node,root)
                count[root] += count[node]
                dist[root] += (dist[node] + count[node])
                            
    def child(root,parent):
        for node in adjacency[root]:
            if node != parent:
                dist[node] = dist[root] - 2* count[node] + n
                child(node,root)            
    counter(0,None)
    child(0,None)            
    return dist

# Sample Input

# Expect [8,12,6,10,10,10]
print(sumOfDistancesInTree(6,[[0,1],[0,2],[2,3],[2,4],[2,5]]))

# Expect [0]
print(sumOfDistancesInTree(1,[]))

# Expect [1,1]
print(sumOfDistancesInTree(2,[[1,0]]))

# Expect [6,4,4,6]
print(sumOfDistancesInTree(4,[[2,0],[3,1],[2,1]]))


""" def sumOfDistancesInTree(n, edges):
    lengths = [[0 for _ in range(n)] for _ in range(n)]
    dist = [0 for _ in range(n)]
    seen = collections.defaultdict(set)
    for elem in edges:
        a , b = elem[0], elem[1]
        lengths[a][b] = lengths[b][a] = 1        
        for nodes in seen[a]:
            if nodes in seen[b]:
                continue
            lengths[nodes][b] = lengths[nodes][a] +1
            lengths[b][nodes] = lengths[nodes][b]
            dist[nodes] += lengths[nodes][b]
            dist[b] += lengths[nodes][b]
            seen[nodes].add(b)
            seen[b].add(nodes)
        for nodes in seen[b]:
            if nodes not in seen[a]:
                lengths[nodes][a] = lengths[nodes][b] +1
                lengths[a][nodes] = lengths[nodes][a]
                dist[nodes] += lengths[nodes][a]
                dist[a] += lengths[nodes][a]
                seen[nodes].add(a)
                seen[a].add(nodes)            
            for nbh in seen[a]:
                if nbh in seen[nodes] or nbh == nodes:
                    continue
                lengths[nbh][nodes] = lengths[nodes][b] + lengths[nbh][a] + 1
                lengths[nodes][nbh] = lengths[nbh][nodes]
                dist[nbh] += lengths[nbh][nodes]
                dist[nodes] += lengths[nbh][nodes]
                seen[nodes].add(nbh)
                seen[nbh].add(nodes)
                print(nbh,nodes)
        seen[b].add(a)
        seen[a].add(b)
        dist[a] +=1
        dist[b] +=1
    return dist """