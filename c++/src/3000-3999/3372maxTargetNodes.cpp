#include "lc_pub.h"


class Solution {
    public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        int n=edges1.size() + 1, m=edges2.size() + 1;
        unordered_map<int, vector<int>> g1;
        unordered_map<int, vector<int>> g2;
        for (auto & edge: edges1){
            g1[edge[0]].emplace_back(edge[1]);
            g1[edge[1]].emplace_back(edge[0]);
        }
        for (auto & edge: edges2){
            g2[edge[0]].emplace_back(edge[1]);
            g2[edge[1]].emplace_back(edge[0]);
        }
        auto dfs = [&](this auto&& dfs, unordered_map<int, vector<int>> &g, int x, int fa, int d) -> int {  // 当前节点为x，父节点为fa，距离为d，返回在此范围内的节点个数
            int res = 1;
            if (d == 0) return res;
            if (d < 0) return 0;
            for (int y: g[x]) {
                if (y == fa) continue;
                res += dfs(g, y, x, d - 1);
            }
            return res;
        };
        int c2 = 0;
        for (int i=0;i<m;i++) {
            c2 = max(c2, dfs(g2,i,-1,k-1));
        }
        vector<int>ans(n);
        for (int i=0;i<n;i++) {
            int c1 = dfs(g1,i,-1,k);
            ans[i] = c1+c2;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> edge1 = parseGrid("[[0,1],[0,2],[2,3],[2,4]]");
    vector<vector<int>> edge2 = parseGrid("[[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]");

    Solution so;
    cout << so.maxTargetNodes(edge1, edge2, 2) << endl;
    return 0;
}
