#include "lc_pub.h"

using namespace std;

class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        int ans=0;
        auto dfs = [&](this auto&& dfs, TreeNode* node, int v) {
            int res = (v << 1) + node->val;
            if (!node->left && !node->right) {
                ans+=res;
                return;
            }
            if (node->left) dfs(node->left, res);
            if (node->right) dfs(node->right, res);
        };
        dfs(root, 0);
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> arrays = parseGrid("[[1,2,3],[4,5],[1,2,3]]");
    Solution so;
    return 0;
}