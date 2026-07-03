class Node:

    def __init__(self, key = 0, value = 0) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.kv = {} # {key: Node}
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head

    def add(self, newNode):
        prv, nxt = self.tail.left, self.tail
        prv.right = nxt.left = newNode
        newNode.left, newNode.right = prv, nxt

    def remove(self, oldNode):
        prv = oldNode.left
        nxt = oldNode.right
        prv.right, nxt.left = nxt, prv

    def get(self, key: int) -> int:
        if key in self.kv:
            self.remove(self.kv[key])
            self.add(self.kv[key])
            return self.kv[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            node = self.kv[key]
            node.value = value
            self.remove(node)
            self.add(node)
            return
        self.kv[key] = Node(key, value)
        self.add(self.kv[key])
        if len(self.kv) > self.cap:
            lru = self.head.right
            del self.kv[lru.key]
            self.remove(lru)

