import random
import math

class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.length = len(w)
        for i in range(self.length):
            self.total += w[i]
        table = [self.length*w[i] / self.total for i in range(self.length)]
        underfull = []
        overfull = []
        for i in range(self.length):
            if table[i] > 1:
                overfull.append(i)
            elif table[i] < 1:
                underfull.append(i)
        self.index = {}
        while overfull and underfull:
            i = overfull.pop(-1)
            j = underfull.pop(-1)
            self.index[j] = i
            table[i] = table[i] + table[j] - 1
            if table[i] < 1:
                underfull.append(i)
            elif table[i] > 1:
                overfull.append(i)        
        self.data = table
        

    def pickIndex(self) -> int:
        x = random.random()
        i = math.floor(x*self.length) 
        y = x * self.length - i 
        if y < self.data[i]:
            return i
        else: 
            return self.index[i]

# beats 95%
# see https://pandasthumb.org/archives/2012/08/lab-notes-the-a.html for explanation