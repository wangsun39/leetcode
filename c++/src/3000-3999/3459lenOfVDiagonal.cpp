#include "lc_pub.h"


class Solution {
    public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int dir[4][2] = {{-1,-1},{1,1},{1,-1},{-1,1}};
        int t[] = {3,2,0,1}; //  方向转换
        int r=grid.size(),c=grid[0].size();
        vector<vector<vector<int>>> memo = vector<vector<vector<int>>>(r, vector<vector<int>>(c, vector<int>(128, -1)));
        auto dfs = [&](this auto&& dfs, int i, int j, int comp) -> int {
            // comp 高4bit为方向，低4bit为是否转过弯
            if (memo[i][j][comp]!=-1) return memo[i][j][comp];
            int idd=comp>>4;
            int turn=comp&1;
            int res=1;
            int u=i+dir[idd][0],v=j+dir[idd][1];
            if (0<=u&&u<r&&0<=v&&v<c&&grid[u][v] + grid[i][j] == 2) res=max(res,1+dfs(u,v,comp));
            if (!turn) {
                int x0=dir[t[idd]][0],y0=dir[t[idd]][1];
                u=i+x0;
                v=j+y0;
                if (0<=u&&u<r&&0<=v&&v<c&&grid[u][v] + grid[i][j] == 2) res=max(res,1+dfs(u,v,(t[idd]<<4)|1));
            }
            memo[i][j][comp] = res;
            return res;
        };

        int ans=0;
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                if (grid[i][j]==1) {
                    ans = max(ans, 1);
                    for (int k=0;k<4;k++) {
                        int u=i+dir[k][0],v=j+dir[k][1];
                        if (0<=u&&u<r&&0<=v&&v<c&&grid[u][v] == 2)
                            ans=max(ans,1+dfs(u,v,k<<4));
                    }
                }
            }
        }
        return ans;
    }
    
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto nums = parseGrid("[[1,2,2],[1,2,0],[0,2,1]]");;

    Solution so;
    cout<<so.lenOfVDiagonal(nums)<<endl;
    return 0;
}
