#include "lc_pub.h"

unordered_set<long long> sp2;

class Solution {
    public:
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        unordered_map<int, int> down;  // 距离叶子

        auto dfs1 = [&](this auto&& dfs1, TreeNode* node) -> int {
            int l=0, r=0;
            if (node->left) l = dfs1(node->left);
            if (node->right) r = dfs1(node->right);
            down[node->val] = 1 + max(l, r);
            return down[node->val];
        };

        dfs1(root);        

        auto dfs2 = [&](this auto&& dfs2, TreeNode* node) -> TreeNode* {
            int l=0, r=0;
            cout<<node->val<<endl;
            // vn[node->val] = node;
            if (node->left) l = down[node->left->val];
            if (node->right) r = down[node->right->val];
            if (l > r) return dfs2(node->left);
            if (l < r) return dfs2(node->right);
            return node;
        };
        return dfs2(root);
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}