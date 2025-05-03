#include "lc_pub.h"

using namespace std;

class Solution {
public:
TreeNode* lcaDeepestLeaves(TreeNode* root) {
    unordered_map<int, int>dep;

    auto dfs = [&](this auto&& dfs, TreeNode *node) -> int {
        // 返回node的最大深度
        if (!node) return 0;
        int l = dfs(node->left);
        int r = dfs(node->right);
        dep[node->val]=max(l,r)+1;
        return dep[node->val];
    };
    dfs(root);

    auto dfs2 = [&](this auto&& dfs2, TreeNode *node, int exp_dep) -> TreeNode* {
        // 返回node的最大深度
        if (dep[node->val]!=exp_dep) return nullptr;
        if (!node->left&&!node->right) return node;
        if (!node->left || dep[node->left->val]!=exp_dep-1) return dfs2(node->right, exp_dep-1);
        if (!node->right || dep[node->right->val]!=exp_dep-1) return dfs2(node->left, exp_dep-1);
        return node;
    };

    return dfs2(root, dep[root->val]);
}
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> arrays = parseGrid("[[1,2,3],[4,5],[1,2,3]]");
    Solution so;
    return 0;
}