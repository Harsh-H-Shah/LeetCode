# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if head==None or head.next==None:
        #     return head
        # pivot = head
        # end = head
        # listlen = 0
        # while(end.next):
        #     end = end.next
        #     listlen+=1
        # listlen+=1
        # k = k%listlen
        # start = listlen-k
        # print(start)
        # while(start-1):
        #     pivot = pivot.next
        #     start-=1
        # new_head = pivot.next
        # pivot.next = None
        # end.next = head
        # return new_head
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
        
        