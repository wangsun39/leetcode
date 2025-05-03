#include "lc_pub.h"


// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
public:
int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
    int MOD=1'000'000'007;
    int dir[4][2] = {{0, 1},{1,0},{0,-1},{-1,0}};
    // const int M=m,N=n,MM=maxMove;
    // int vis[M][N][MM + 1];
    int vis[50][50][50 + 1];
    memset(vis, -1, sizeof(vis));
    auto dfs = [&](this auto&& dfs, int r, int c, int k) -> int {
        // 在位置r,c处，剩余移动次数为k时，总的移动次数
        if (vis[r][c][k]!=-1) return vis[r][c][k];
        if (k==0) {
            return vis[r][c][k]=0;
        }
        long long res=0;
        for (int i=0;i<4;i++) {
            int x=r+dir[i][0],y=c+dir[i][1];
            if (0<=x&&x<m&&0<=y&&y<n) {
                res+=dfs(x,y,k-1);
                res%=MOD;
            }
            else res++;
        }
        return vis[r][c][k]=res%MOD;
    };
    // int ans=dfs(startRow,startColumn,maxMove);
    // return ans;
    return dfs(startRow,startColumn,maxMove);
}
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    auto v = so.findPaths(2,2,2,0,0);
    cout << v << endl;
    return 0;
}
