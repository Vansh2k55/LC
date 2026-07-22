
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        smallDummy = ListNode(0)
        largeDummy = ListNode(0)
        small = smallDummy
        large = largeDummy
        curr=head
        while curr:
            if curr.val<x:
                small.next=curr
                small=small.next
            else:
                large.next=curr
                large=large.next
            curr=curr.next
        small.next=largeDummy.next
        large.next=None

        return smallDummy.next
      
        