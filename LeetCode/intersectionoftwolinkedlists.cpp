// Two-Pointers Solution
// Time Complexity: O(m+n)
// Space Complexity: O(1)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* startA = headA;
        ListNode* startB = headB;
        while (startA != startB)    
        {
            if (startA == nullptr) {
                startA = headB;
            }
            else {
                startA = startA->next;
            }
            
            if (startB == nullptr) {
                startB = headA;
            }
            else {
                startB = startB->next;
            }
        }
        return startA; // if startA == startB
    }
};