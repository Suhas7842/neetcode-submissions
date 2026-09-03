from collections import defaultdict

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def insert(self, node):
        # Insert at the MRU end (before right)
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def remove_lru(self):
        # First real node is the least recently used
        node = self.left.next
        self.remove(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # key -> Node
        self.cache = {}
        # frequency -> DoublyLinkedList
        self.freq_map = defaultdict(DoublyLinkedList)
        self.min_freq = 0

    def update_frequency(self, key):
        node = self.cache[key]
        old_freq = node.freq
        # Remove from the old frequency list
        self.freq_map[old_freq].remove(node)
        # If this was the last node with min_freq,
        # increase min_freq
        if (
            old_freq == self.min_freq
            and self.freq_map[old_freq].size == 0
        ):
            self.min_freq += 1
        # Increase frequency
        node.freq += 1
        # Add to the new frequency list
        self.freq_map[node.freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.update_frequency(key)
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        # Key already exists
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.update_frequency(key)
            return
        # Cache is full
        if len(self.cache) >= self.capacity:
            # Get the LRU node among the least frequently used nodes
            lru_node = self.freq_map[self.min_freq].remove_lru()
            del self.cache[lru_node.key]
        # Create new node
        node = Node(key, value)
        self.cache[key] = node
        # New nodes have frequency 1
        self.freq_map[1].insert(node)
        # Frequency 1 is now the minimum
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)