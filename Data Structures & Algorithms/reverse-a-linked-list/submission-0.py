# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previousNode, currentNode = None, head

        while currentNode:
            t = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = t

        return previousNode