# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        point = head
        seen = set()
        while(point):
            if point in seen:
                return True
            seen.add(point)
            point = point.next
        return False