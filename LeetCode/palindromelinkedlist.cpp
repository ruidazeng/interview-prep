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

// Reverse the linked list from start till middle of linked list
// Then we can simple match each element in the first half and second half

// Find middle of linked list can be found using the slow-fast pointer approach

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* prev = nullptr;
        ListNode* tmp;
        
        while (fast && fast->next) {
            // move fast pointer
            fast = fast->next->next;
            // move slow and also reverse the linked list
            tmp = slow->next;
            slow->next = prev;
            // update prev before updating slow
            prev = slow;
            slow = tmp;
        }
        
        // if fast == nullptr, the linked list is even length
        // if fast == number, or fast != nullptr, the linked list is odd length
        // if odd length, move slow forward to ignore the middle element
        if (fast) {
            slow = slow->next;
        }
        
        // now reverse and compare
        while (slow) {
            if (prev->val != slow->val) {
                return false;
            }
            prev = prev->next;
            slow = slow->next;
        }
        
        return true;
    }
};