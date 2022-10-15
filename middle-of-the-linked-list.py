class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer1=head
        pointer2=head
        while  pointer2 and pointer2.next:
            pointer1=pointer1.next
            pointer2=pointer2.next.next
        return pointer1
