class ListNode:
    def __init__(self,key,val,next=None,prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    def get(self, key: int) -> int:
        if key in self.store.keys():
            self.remove(self.store[key])
            self.insert(self.store[key])
            return self.store[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])
        self.store[key] = ListNode(key,value)
        self.insert(self.store[key])
        if len(self.store)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.store[lru.key]
        
    def insert(self,node):
        nxt = self.right
        prev = self.right.prev
        node.next = nxt
        nxt.prev = node
        prev.next = node
        node.prev = prev
    def remove(self,node):
        nxt = node.next
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev