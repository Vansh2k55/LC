# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=ListNode(0)
        ptr=temp
        cur=head
        while cur:
            if cur.val!=val:
                ptr.next=cur
                ptr=ptr.next
            cur=cur.next
        ptr.next=None
            
        return temp.next

        