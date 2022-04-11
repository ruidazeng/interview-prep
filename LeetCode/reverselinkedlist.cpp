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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* next;
        while (head) {
            next = head->next; // save next
            head->next = prev; // reverse head->next
            prev = head; // save current head
            head = next; // move onto next node
        }
        return prev; // return head that is not nullptr
    }
};