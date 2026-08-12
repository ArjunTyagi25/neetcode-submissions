class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}

        # left: LRU, right: MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove node from the linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev, node.next = None, None


    # Insert at the right-most position
    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev

        self.right.prev.next = node
        self.right.prev = node
        

    def get(self, key: int) -> int:
        # Check the hash_map to find the node
        if key in self.key_to_node:
            # Remove the node from the linked list
            self.remove(self.key_to_node[key])
            # Insert the node to the rightmost position in linked list
            self.insert(self.key_to_node[key])
            # Return the value
            return self.key_to_node[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.remove(self.key_to_node[key])

        self.key_to_node[key] = Node(key, value)
        self.insert(self.key_to_node[key])

        if len(self.key_to_node) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.key_to_node[LRU.key]

        
