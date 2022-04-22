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
        if(!head) return nullptr;
        ListNode *i = nullptr, *j = head;
        int diff_pos = 0;
        while(j!=nullptr)
        {
            if(diff_pos<n) {
                diff_pos++;
                j = j->next;
            }
            else{
                i = (i==nullptr) ? head : i->next;
                j = j->next;
            }
        }
        if(!i) {
            head = head->next;
            return head;
        }
        i->next = i->next->next;
        return head;
    }
};