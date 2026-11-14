class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.next: Node | None = None


class MyHashMap:
    def __init__(self) -> None:
        self.capacity = int(1e4)
        self.map = [Node(0, 0) for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        index = key & (self.capacity - 1)
        node = self.map[index]
        while node.next:
            if node.next.key == key:
                node.next.value = value
                return
            node = node.next
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        index = key & (self.capacity - 1)
        node = self.map[index]
        while node.next:
            if node.next.key == key:
                return node.next.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = key & (self.capacity - 1)
        node = self.map[index]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)