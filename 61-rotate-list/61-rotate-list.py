# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        copy = head
        size = 1
        while copy.next:
            size+=1
            copy = copy.next
        k = k%size if k>=size else k
        if k==0:
            return head
        else:
            copy.next = head
        
        # move to a point where we need to cut the link
        ctr = 1
        while ctr<size-k:
            head = head.next
            ctr+=1
        # store the value to return and remove the link
        temp = head.next
        head.next = None
        return temp
        
        