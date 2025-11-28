#include "lc_pub.h"

class Solution {
    public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        vector<vector<int>> g(n);
        for (auto& edge: edges) {
            g[edge[0]].push_back(edge[1]);
            g[edge[1]].push_back(edge[0]);
        }
        int ans=0;
        auto dfs = [&](this auto&& dfs, int x, int fa) -> long long {
            long long res=0;
            for (int y: g[x]) {
                if (y==fa) continue;
                res += dfs(y, x);
            }
            res += values[x];
            ans += (res % k == 0);
            return res;
        };
        dfs(0, -1);
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,0,6,1,5,2,1};
    auto edges = parseGrid("[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]");

    Solution so;
    cout << so.maxKDivisibleComponents(7,edges,nums,3) << endl;
    return 0;
}
