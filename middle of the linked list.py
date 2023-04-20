class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
       current1=head
       current2 = head
       while current2 and current2.next:
           current1=current1.next
           current2=current2.next.next
       return current1
