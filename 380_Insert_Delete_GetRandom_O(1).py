class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.elems = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.elems:
            return False
        else:
            self.elems[val] = self.length
            self.list.append(val)
            self.length += 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.elems:
            index = self.elems[val] 
            last = self.list[-1]
            self.list[index] = last
            self.list.pop()
            self.elems[last] = index
            del self.elems[val]
            self.length -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        x = random.random()
        return self.list[math.floor(x * self.length)]


# Sample Inputs
obj = RandomizedSet()
print(obj.insert(0))
print(obj.elems)
print(obj.list)

print(obj.remove(0))
print(obj.elems)
print(obj.list) 

print(obj.insert(-1))
print(obj.elems)
print(obj.list)

print(obj.remove(0))
print(obj.elems)
print(obj.list)
