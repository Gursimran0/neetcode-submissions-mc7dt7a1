class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.store = []
        

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        self.store.append(val)
        self.hashMap[val] = len(self.store)-1
        return True
    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        valIndex = self.hashMap[val]
        lastIndexVal = self.store[-1]
        self.store[valIndex] = lastIndexVal
        self.store[-1] = val
        self.hashMap[lastIndexVal] = valIndex
        del self.hashMap[val]
        self.store.pop()
        return True
    def getRandom(self) -> int:
        return random.choice(self.store)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()