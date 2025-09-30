#include "lc_pub.h"

using namespace std;

class Solution {
    public:
    int minScoreTriangulation(vector<int>& values) {
        unordered_map<long long, int>vis;
        auto dfs = [&](this auto&& dfs, int i, int j) -> int {
            long long v=((long long)i<<32) + j;
            if (vis.find(v)==vis.end()) return vis[v];
            int res=INT_MAX;
            if (i+1==j) return 0;
            for (int k=i+1;k<j;k++) {
                res = min(res, values[i]*values[j]*values[k]+dfs(i,k)+dfs(k,j));
            }
            vis[v] = res;
            return res;
        };
        return dfs(0, values.size()-1);
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr{1,2,3};
    Solution so;
    so.minScoreTriangulation(arr);
    return 0;
}