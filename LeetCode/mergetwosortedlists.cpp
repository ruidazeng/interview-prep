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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        // Initialize results
        ListNode* temp = new ListNode();
        ListNode* merged = temp;
        
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                temp->next = list1;
                list1 = list1->next;
            }
            else {
                temp->next = list2;
                list2 = list2->next;
            }
            // traverse linked list
            temp = temp->next;
        }
        
        // Base Cases
        if (list1 == nullptr) {
            temp->next = list2;
        }
        if (list2 == nullptr) {
            temp->next = list1;
        }
        
        // final list
        return merged->next;
    }
};