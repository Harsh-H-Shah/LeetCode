# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow = ListNode()
        slow.next = head
        point = slow
        fast = head
        while(fast and fast.next):
            if fast.val==fast.next.val:
                val = fast.val
                while fast and fast.val==val:
                    fast.val = -101
                    fast = fast.next
            else:
                fast = fast.next
        fast = head
        while(fast and fast.next):
            if fast.val!=-101:
                slow.next = fast
                fast = fast.next
                slow = slow.next
            else:
                fast = fast.next
        if fast.val==-101:
            slow.next = None
        else:
            slow.next = fast
        return point.next
                