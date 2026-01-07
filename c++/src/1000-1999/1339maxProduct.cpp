#include "lc_pub.h"


class Solution {
    
    public:
    int maxProduct(TreeNode* root) {
        vector<int> sums;
        long long s = 0;
        auto dfs = [&](this auto&& dfs, TreeNode* node) -> long long {
            if (!node) return 0;
            long long l = dfs(node->left);
            long long r = dfs(node->right);
            long long res = l + r + node->val;
            sums.push_back(res);
            s+=node->val;
            return res;
        };
        dfs(root);
        long long mx = 0;
        for (int x: sums) {
            mx=max(mx, (s-x)*x);
        }
        return mx % int(1e9+7);
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}
