#include "lc_pub.h"

using namespace std;

class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        vector<long long> s(1, 0);
        long long mx=INT_MIN;
        int ans = 0;
        auto dfs = [&](this auto&& dfs, TreeNode* node, int lv) {
            if (!node) return;
            if (s.size()<=lv) {
                s.push_back(node->val);
            }
            else
            {
                s[lv]+=node->val;
            }

            dfs(node->left, lv+1);
            dfs(node->right, lv+1);
        };
        dfs(root, 1);
        for (int i=1;i<s.size();i++) {
            if (mx <s[i]) {
                mx=s[i];
                ans=i;
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}