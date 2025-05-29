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
        vector<int> c1(n, 0);  // g1 每个点涂色
        vector<int> c2(m, 0);  // g2 每个点涂色
        auto dfs = [&](this auto&& dfs, unordered_map<int, vector<int>> &g, int x, int fa, int d, vector<int> &c) -> void {  // 当前节点为x，父节点为fa，颜色为d，返回在此范围内的节点个数
            int res = 1;
            c[x] = d;
            for (int y: g[x]) {
                if (y == fa) continue;
                dfs(g, y, x, d ^ 1, c);
            }
        };
        dfs(g1, 0, -1, 0, c1);
        dfs(g2, 0, -1, 0, c2);
        int c10=0,c11=0;
        for (auto x: c1)
            if (x) c11++;
            else c10++;
        int c20=0,c21=0;
        for (auto x: c2)
            if (x) c21++;
            else c20++;
        int c2max = max(c20, c21);

        vector<int>ans(n);
        for (int i=0;i<n;i++) {
            if (c1[i])
                ans[i] = c11 + c2max;
            else
                ans[i] = c10 + c2max;
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
