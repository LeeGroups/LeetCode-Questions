class node:
    def __init__(self, key = 0, value = 0, node1 = None, node2 = None):
        self.previous = node1
        self.next = node2
        self.key = key     
        self.value = value
        
class LRUCache:   
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.length = 0
        self.data = None
        self.last = None
        self.elems = {} 
    
    def remove(self):
        u = self.last.key
        self.last = self.last.previous     
        self.last.next = None
        del self.elems[u]
    
    def move(self,key):
        if self.length != 1 and self.data.key != key:
            x = self.elems[key].previous
            y = self.elems[key].next
            x.next = y
            if y != None:
                y.previous = x      
            else:
                self.last = x
            u = node(key, self.elems[key].value, None, self.data)
            self.data.previous = u
            self.data = u
            self.elems[key] = u        
    
    def get(self, key: int) -> int:
        if key in self.elems:
            val = self.elems[key].value        
            self.move(key)
            return val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.elems:
            self.elems[key].value = value
            self.move(key)
        else:             
            if self.length == 0:
                self.data = node(key,value,None,None)
                self.last = self.data
                self.elems[key] = self.data
            else:
                u = node(key, value, None, self.data)
                self.data.previous = u
                self.data = u
                self.elems[key] = u
            self.length += 1

        if self.length > self.cap:
            self.remove()
            self.length -= 1

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))