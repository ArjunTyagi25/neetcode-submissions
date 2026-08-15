class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}

        self.left = self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
               
    # Remove a node from the linked list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev = self.right.prev

        prev.next, node.next = node, self.right
        self.right.prev, node.prev = node, prev

    def get(self, key: int) -> int:
        if key in self.hash_map:
            val = self.hash_map[key].val
            self.remove(self.hash_map[key])
            self.insert(self.hash_map[key])
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
            del self.hash_map[key]

        new_Node = Node(key, value)
        self.hash_map[key] = new_Node
        self.insert(new_Node)

        if len(self.hash_map) > self.capacity:
            del_node = self.left.next
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            del self.hash_map[del_node.key]


        
        

        
