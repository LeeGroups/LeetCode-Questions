def LeftofLine(x,y,z):
    SlopeDiff = (z[1]-x[1])*(y[0]-x[0]) - (z[0]-x[0])*(y[1]-x[1])
    if SlopeDiff == 0:
        return 0
    elif SlopeDiff > 0:
        return 1
    else:
        return -1

def outerTrees(trees):
    EndPoints = []
    First = trees[0]
    for point in trees:
        if point[0] < First[0]:
            First = point
    EndPoints.append(First)
    while True:
        test = trees[0]
        temp = []
        for i in range(len(trees)):
            print(First,test,trees[i],temp,EndPoints)
            if First == trees[i]:
                continue
            if First == test:
                test = trees[i]
            Slope = LeftofLine(First,test,trees[i])            
            if Slope == 1:
                test = trees[i]                
                temp = []
            elif Slope == 0:
                if (First[0]-trees[i][0])**2 + (First[1]-trees[i][1])**2 >= (First[0]-test[0])**2 + (First[1]-test[1])**2:
                    temp.append(test)
                    test = trees[i]      
                else:
                    temp.append(trees[i])         
        
        EndPoints.append(test)
        EndPoints += temp
        if test == EndPoints[0]:
            break
        First = test
    seen = set()
    output = []
    for elem in EndPoints:
        if str(elem) not in seen:
            output.append(elem)
            seen.add(str(elem))
    return output

# Sample Inputs

# Expect [[1,1],[2,0],[3,3],[2,4],[4,2]]
print(outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))

# Expect [[4,2],[2,2],[1,2]]
print(outerTrees([[1,2],[2,2],[4,2]]))
 
# Expect [[3,3],[4,2],[0,2],[1,1],[2,4]]
print(outerTrees([[0,2],[1,1],[2,2],[2,4],[4,2],[3,3]]))
 
# Expect [[7,4],[5,0],[7,3],[2,1],[5,5],[4,5],[3,5],[7,2],[1,2],[1,4],[4,0],[2,5],[6,1],[6,5],[0,3],[3,0]]
print(outerTrees([[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]))
 