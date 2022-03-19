# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = []
        while(head):
            num.append(head.val)
            head = head.next
        ans = 0
        num.reverse()
        print(num)
        if num[0] == 1:
            ans+=1
        for i in range(1,len(num)):
            ans += (num[i]*2)**i
        return ans