/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* p1 = head;
        ListNode* p2 = head;
        int count = 0;
        while(count<n){
            p2 = p2->next;
            count++;
        }
        if(!p2){
            ListNode* temp = head->next;
            delete(head);
            return temp;
        }
        while(p2->next){
            p1 = p1->next;
            p2 = p2->next;
        }
        ListNode* temp = p1->next;
        p1->next = p1->next->next;
        delete(temp);
        return head;
    }
};