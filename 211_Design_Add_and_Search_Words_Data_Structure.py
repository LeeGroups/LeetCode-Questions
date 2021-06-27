import collections
class Trie:
    def __init__(self):
        self.kids = collections.defaultdict(Trie)
        self.fullword = False

class WordDictionary:
    def __init__(self):
        self.data = Trie()

    def addWord(self, word: str) -> None:
        x = self.data
        for i in word:
            x = x.kids[i]
        x.fullword = True

    def search(self, word: str) -> bool:
        def search_helper(trie, word: str) -> bool:
            x = trie
            if word == "":
                return x.fullword
            for i in range(len(word)):
                if word[i] == ".":
                    for child in x.kids:
                        if search_helper(x.kids[child],word[i+1:]):
                            return True
                elif word[i] in x.kids:
                    return search_helper(x.kids[word[i]],word[i+1:])
                return False
        return search_helper(self.data,word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# sample inputs:

#Expect [1,1,2,3,4,4,5,6]
obj1 = WordDictionary()
obj1.addWord("at")
obj1.addWord("and")
obj1.addWord("an")
obj1.addWord("add")
obj1.addWord("can")
obj1.addWord("aq")
obj1.addWord("cu")
obj1.addWord("and")
print("searching a " + str(obj1.search("a")))
print("searching .at " +str(obj1.search(".at"))) 
obj1.addWord("bat")
print("searching .at " +str(obj1.search(".at")))
print("searching an. " +str(obj1.search("an.")))
print("searching a.d. " +str(obj1.search("a.d.")))
print("searching b. " +str(obj1.search("b.")))
print("searching a.d " +str(obj1.search("a.d")))
print("searching . " +str(obj1.search(".")))



""" class WordDictionary:
    def __init__(self):
        Initialize your data structure here.
        self.data = []
        self.length = 0

    def addWord(self, word: str) -> None:
        first = 0
        last = self.length
        n = len(word)
        added = False
        while first != last:
            middle = (last - first) //2 + first
            if self.data[middle] == word:
                added = True
                break 
            elif len(self.data[middle]) > n:
                last = middle
            elif len(self.data[middle]) < n:
                first = middle +1
            elif self.data[middle] > word:
                last = middle
            else: 
                first = middle + 1
        if not added:
            self.data.insert(first,word)
            self.length += 1
        
    def search(self, word: str) -> bool:
        first1, first2 = 0 , 0
        last1, last2 = self.length, self.length
        n = len(word)
        while first1 != last1 or first2 !=last2:
            if first1 != last1: 
                middle1 = (last1 - first1) //2 + first1
                if self.data[middle1] == word:
                    return True
                if len(self.data[middle1]) > n:
                    last1 = middle1
                elif len(self.data[middle1]) < n:
                    first1 = middle1 +1
                else:
                    if middle1 == 0 or len(self.data[middle1-1]) < n:
                        last1 = middle1
                        first1 = middle1
                    else:
                        last1 = middle1
            if first2 != last2:
                middle2 = (last2 - first2) //2 + first2
                if self.data[middle2] == word:
                    return True
                if len(self.data[middle2]) > n:
                    last1 = min(last1,middle2)
                    last2 = middle2
                elif len(self.data[middle2]) < n:
                    first1 = max(first1,middle2)
                    first2 = middle2+1
                else:
                    if middle2 >= self.length or len(self.data[middle2])>n:
                        first2 = middle2 
                        last2 = middle2 
                    else:
                        first2 = middle2 +1
        u = [i for i in range(first1,first2)]
        for j in range(len(u)):
            print(self.data[u[j]])
        for i in range(len(word)):            
            if u == []:
                return False
            elif word[i] == ".": continue
            else: 
                for j in range(len(u)-1,-1,-1):
                    if self.data[u[j]][i] != word[i]:
                        u.pop(j)
        return u != []  """
