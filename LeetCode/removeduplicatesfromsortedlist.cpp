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
    ListNode* deleteDuplicates(ListNode* head) {
        int prev_val = -1;
        ListNode* start_head = head;
        ListNode* prev_head = head;
        
        while (head != nullptr) {
            if (head->val == prev_val) {
                prev_head->next = head->next;
            }
            else {
                prev_head = head;
            }
            prev_val = head->val;
            head = head->next;
        }
        
        return start_head;
        
    }
};