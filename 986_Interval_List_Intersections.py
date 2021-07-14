def intervalIntersection(firstList, secondList):
    def helper(list1, list2):
        overlap = []
        n = list1[0][1]
        for i in range(len(list2)):
            if list2[i][0] <= n:
                if list2[i][1] <= n:
                    overlap.append(list2[i])
                else:
                    overlap.append([list2[i][0],n])
                    return (overlap, i)
            else:
                return (overlap,i)
        return (overlap,len(list2))
    output = []        
    i = 0 
    j = 0 
    while i < len(firstList) and j < len(secondList):
        print(i,j)
        if firstList[i][0] <= secondList[j][0]:
            overlap, k = helper(firstList[i:],secondList[j:])
            output.extend(overlap)
            i += 1
            j += k
        else:
            overlap, k = helper(secondList[j:],firstList[i:])
            output.extend(overlap)
            j += 1
            i += k
    return output

#sample inputs

# expect [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))

# expect []
print(intervalIntersection([[1,3],[5,9]],[]))

# expect []
print(intervalIntersection([],[[4,8],[10,12]]))

# expect [[3,7]]
print(intervalIntersection([[1,7]],[[3,10]]))

# expect [[5,10]]
print(intervalIntersection([[3,10]],[[5,10]]))