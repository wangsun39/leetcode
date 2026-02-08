#include "lc_pub.h"

class Solution {
    
    public:
    bool isBalanced(TreeNode* root) {
        auto dfs = [&](this auto&& dfs, TreeNode* node) -> int {
            if (!node) return 0;
            int l=dfs(node->left),r=dfs(node->right);
            if (l==-1||r==-1) return -1;
            if (abs(l-r)>1) return -1;
            return max(l,r)+1;
        };
        int ans=dfs(root);
        return ans!=-1;
        
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}
