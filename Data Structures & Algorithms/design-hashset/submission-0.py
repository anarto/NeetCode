class ListNode:
    def __init__(self, value=-1):
        self.value  = value;
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode() for i in range(10000)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.value == key:
                return
            cur = cur.next

        cur.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.value == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.value == key:
                return True
            cur = cur.next
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)