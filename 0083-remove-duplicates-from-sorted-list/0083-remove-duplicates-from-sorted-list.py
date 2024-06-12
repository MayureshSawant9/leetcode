# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        current = head
        while current:
            if current.val == prev.val:
                prev.next = current.next

            else:
                prev = prev.next
            
            current = current.next

        return head
            