class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = node(0,0)
        self.right = node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def remove(self,node):
        nxt = node.next
        prv = node.prev
        nxt.prev = prv
        prv.next = nxt
    def insert(self,node):
        nxt = self.right
        prv = nxt.prev
        prv.next = node
        node.prev = prv
        node.next = nxt
        nxt.prev = node
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
        
class node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None