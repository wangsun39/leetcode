#include "lc_pub.h"

using namespace std;

class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        vector<long long> s(1, 0);
        long long mx=0;
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
            if (s[lv]>mx) {
                mx = s[lv];
                ans=lv;
            }
            else if (s[lv]==mx) {
                ans=min(ans,lv);
            }
            dfs(node->left, lv+1);
            dfs(node->right, lv+1);
        };
        dfs(root, 1);
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> arrays = parseGrid("[[2,1],[5,4],[3,7],[6,2],[4,4],[1,8],[9,6],[5,3],[7,4],[1,9],[1,1],[6,6],[9,6],[1,3],[9,7],[4,7],[5,1],[6,5],[1,6],[6,1],[1,8],[7,2],[2,4],[1,6],[3,1],[3,9],[3,7],[9,1],[1,9],[8,9]]");
    Solution so;
    std::cout<<so.numEquivDominoPairs(arrays)<<endl;
    return 0;
}