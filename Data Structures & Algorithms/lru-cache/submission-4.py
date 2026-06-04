class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.head=Node(0,0)
        self.tail=Node(0,0)

        self.head.next=self.tail
        self.tail.prev=self.head
    
    def remove(self,node):
        prev_node=node.prev
        next_node=node.next

        prev_node.next=next_node
        next_node.prev=prev_node

    def insert_at_end(self,node):
        prev_last=self.tail.prev

        prev_last.next=node
        node.prev=prev_last

        node.next=self.tail
        self.tail.prev=node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert_at_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value

            self.remove(node)
            self.insert_at_end(node)
            return
            
        node=Node(key,value)
        self.cache[key]=node
        self.insert_at_end(node)

        if len(self.cache)>self.capacity:
            lru=self.head.next
            self.remove(lru)
            del self.cache[lru.key]
