/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> answer;
        stack<TreeNode*> todo;
        
        while (root || !todo.empty()) {
            while (root) {
                todo.push(root);
                answer.push_back(root->val);
                root = root->right;
            }
            root = todo.top();
            todo.pop();
            root = root->left;
        }
        std::reverse(answer.begin(),answer.end());
        return answer;
    }
};