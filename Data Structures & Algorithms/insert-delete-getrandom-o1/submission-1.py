class RandomizedSet:

    def __init__(self):
        self.numsToIndex = {}
        self.values = []
        

    def insert(self, val: int) -> bool:
        if val in self.numsToIndex:
            return False
        self.numsToIndex[val] = len(self.values)
        self.values.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.numsToIndex:
            return False
        index = self.numsToIndex[val]
        self.values[index] = self.values[-1]
        self.numsToIndex[self.values[-1]] = index
        self.values.pop()
        del self.numsToIndex[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()