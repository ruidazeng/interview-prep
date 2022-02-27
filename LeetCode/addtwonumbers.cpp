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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = nullptr; // res is head node of the resultant list
        ListNode *temp, *prev = nullptr;
        int carry = 0, sum;
        while(l1 != nullptr || l2 != nullptr) {
            sum = carry + (l1? l1->val: 0) + (l2? l2->val: 0);
            // update sum and carry
            carry = (sum >= 10)? 1 : 0;
            sum = sum % 10;
            // Create a new node with sum as data
            temp = new ListNode(sum);

            if (res == nullptr) {
                res = temp;
            }
            else {
                prev->next = temp;
            }
            prev = temp;
            // Move first and second pointers to next nodes
            if (l1 != nullptr) {
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                l2 = l2->next;
            }
        }
        // last process: create node for carry
        if (carry > 0) {
            temp->next = new ListNode(carry);
        }
        return res;
    }
};
