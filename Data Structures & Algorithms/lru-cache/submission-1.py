class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # 初始化两个哨兵节点：head (最久未使用), tail (最近使用)
        # 真正的节点都在 head 和 tail 之间
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # 辅助函数：从链表中移除节点
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # 辅助函数：添加节点到链表末尾（变成最新的）
    def _add(self, node):
        # 这里的顺序很重要：要插在 self.tail 之前
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 1. 先把它从当前位置删掉
            self._remove(node)
            # 2. 再把它加到末尾（变成最近使用的）
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果 key 存在，先删除旧节点
            self._remove(self.cache[key])
        
        # 创建新节点并存入 cache
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node

        # 检查是否超容
        if len(self.cache) > self.capacity:
            # 要删除的是 head 后面的第一个节点（最久未使用的）
            lru_node = self.head.next
            self._remove(lru_node)
            # 别忘了从字典里也删掉！这是你原来漏掉的关键一步
            del self.cache[lru_node.key]