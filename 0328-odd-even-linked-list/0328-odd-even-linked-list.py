# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        list1=ListNode(0)
        list2=ListNode(0)
        curr1=list1
        curr2=list2
        curr=head
        pos=1

        while curr:
            if pos%2==1:
                curr1.next=curr
                curr1=curr1.next
            else:
                curr2.next=curr
                curr2=curr2.next
            pos+=1
            curr=curr.next
        curr2.next=None
        curr1.next=list2.next
        return list1.next

        