#include "lc_pub.h"

int cand[12][3] = {{1,2,1},{2,1,2},{3,1,2},{1,2,3},{2,1,3},{3,1,3},{1,3,1},{2,3,1},{3,2,1},{1,3,2},{2,3,2},{3,2,3}};
unordered_map<int,vector<int>> nxt;

auto init = [] {
    for (int i=0;i<12;i++) {
        for (int j=0;j<12;j++) {
            if (cand[i][0]!=cand[j][0]&&cand[i][1]!=cand[j][1]&&cand[i][2]!=cand[j][2]) {
                nxt[i].push_back(j);
            }
        }
    }
    return 0;
}();

class Solution {
public:
    int numOfWays(int n) {
        int MOD=1e9+7;
        vector<vector<int>> mem(n, vector<int>(12,0));

        auto dfs = [&](this auto&& dfs, int i, int j) -> int {  // 从第i+1项开始，第i项的顺序(在cand中的下标)下标为j
            long long res=0;
            if (mem[i][j]) return mem[i][j];
            if (i==n-1) {
                // mem[i][j]=nxt[j].size();
                // return nxt[j].size();
                return 1;
            }
            for (auto k: nxt[j]) {
                res += dfs(i+1,k);
                res%=MOD;
            }
            mem[i][j]=res;
            return res;
        };
        long long ans=0;
        for (int i=0;i<12;i++) {
            ans+=dfs(0,i);
            ans%=MOD;
        }
        return ans;
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};
    
    Solution so;
    cout << so.numOfWays(1) << endl;
    return 0;
}
