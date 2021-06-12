
def kClosest(points,k):
    return sorted(points, key= lambda x: x[0]*x[0]+x[1]*x[1])[:k]

# sample inputs:

#Expect [[-2,2]]
print( kClosest([[1,3],[-2,2]],1))

#Expect [[3,3],[-2,4]]
print( kClosest([[3,3],[5,-1],[-2,4]],2))
