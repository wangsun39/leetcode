#include "lc_pub.h"
const long long INF = LLONG_MAX / 2; // 防止加法溢出
vector<vector<long long>> shortestPathFloyd(int n, vector<vector<int>>& edges) {
    
    vector f(n, vector<long long>(n, INF));
    for (int i = 0; i < n; i++) {
        f[i][i] = 0;
    }

    for (auto& e : edges) {
        int x = e[0], y = e[1];
        long long wt = e[2];
        f[x][y] = min(f[x][y], wt); // 如果有重边，取边权最小值
        // f[y][x] = min(f[y][x], wt); // 无向图
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            if (f[i][k] == INF) { // 针对稀疏图的优化
                continue;
            }
            for (int j = 0; j < n; j++) {
                f[i][j] = min(f[i][j], f[i][k] + f[k][j]);
            }
        }
    }
    return f;
}


class Solution {
    public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        vector<vector<int>> edges;
        int n=cost.size();
        for (int i=0;i<n;i++) {
            edges.push_back({original[i]-'a',changed[i]-'a',cost[i]});
        }
        vector<vector<long long>> f=shortestPathFloyd(26, edges);
        int m=source.size();
        long long ans=0;
        for (int i=0;i<m;i++) {
            if (f[source[i]-'a'][target[i]-'a']==INF) return -1;
            ans+=f[source[i]-'a'][target[i]-'a'];
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<char> nums{'a','b','c','c','e','d'},nums2{'b','c','b','e','b','e'};
    vector<int> cost{2,5,5,1,2,20};

    Solution so;
    cout << so.minimumCost("abcd", "acbe", nums, nums2,cost) << endl;
    return 0;
}
