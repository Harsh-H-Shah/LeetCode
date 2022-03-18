# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare=head
        turtle=head
        while hare!=None and hare.next!=None and turtle!=None:
            hare=hare.next.next
            turtle=turtle.next
            if hare==turtle:
                hare=head
                while hare!=turtle:
                    hare=hare.next
                    turtle=turtle.next
                return hare
        return None