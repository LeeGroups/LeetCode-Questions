def merge(intervals):
    """
    :type n: int
    :rtype: int
    """
    list1 = sorted(intervals, key = lambda x: x[0])
    output = []
    current_first = list1[0][0]
    current_last = list1[0][1]
    for i in range(len(list1)):
        if list1[i][0] <= current_last:
            if list1[i][1] > current_last:
                current_last = list1[i][1]
        else:
            output.append([current_first,current_last])
            current_first = list1[i][0]
            current_last = list1[i][1]
    output.append([current_first,current_last])
    return output

# sample inputs:

#Expect [[1,6],[8,10],[15,18]]
print( merge( [[1,3],[2,6],[8,10],[15,18]]))

#Expect [[1,5]]
print( merge( [[1,4],[4,5]]))

