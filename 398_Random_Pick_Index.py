import collections
import random
import math

class Solution:

    def __init__(self, nums: List[int]):
        self.integers = {}
        for i in range(len(nums)):
            if nums[i] in self.integers:
                self.integers[nums[i]].append(i)
            else:
                self.integers[nums[i]] = [i]

    def pick(self, target: int) -> int:
        x = random.random()
        if target in self.integers:
            n = len(self.integers[target])
            return self.integers[target][math.floor(x*n)]