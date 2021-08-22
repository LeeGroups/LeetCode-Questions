import collections
import copy

def canFinish(numCourses, prerequisites):
    dictionary = collections.defaultdict(set)
    for elem in prerequisites:
        dictionary[elem[0]].add(elem[1])
    ancestor = collections.defaultdict(set)
    seen = set()
    for elem in dictionary:
        if elem in seen:
            continue
        stack = [(course, elem) for course in dictionary[elem]]
        while stack:
            course, previous = stack.pop()
            if course not in ancestor:
                ancestor[course] = copy.deepcopy(ancestor[previous])
            ancestor[course].add(previous)
            if course in dictionary:
                for prereq in dictionary[course]:
                    if prereq in ancestor[course]:
                        return False
                    else:
                        if prereq not in seen:
                            stack.append((prereq,course))
            seen.add(course)
    return True

# beats 84%
    
# Sample Inputs:

# Expect True
print(canFinish(2,[[1,0]]))

# Expect False
print(canFinish(2,[[1,0],[0,1]]))

# Expect True
print(canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))

# Expect True
print(canFinish(7,[[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))