#include "lc_pub.h"

class Solution {
    public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        vector<vector<int>> ans(n, vector<int>(n, 0));
        for (auto & q: queries) {
            int r1=q[0],c1=q[1],r2=q[2],c2=q[3];
            ans[r1][c1]++;
            if (r2+1<n) ans[r2+1][c1]--;
            if (c2+1<n) ans[r1][c2+1]--;
            if (r2+1<n&&c2+1<n) ans[r2+1][c2+1]++;
        }
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                if (j) ans[i][j]+=ans[i][j-1];
            }
            for (int j=0;j<n;j++) {
                if (i) ans[i][j]+=ans[i-1][j];
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto q=parseGrid("[[1,1,2,2],[0,0,1,1]]");

    Solution so;
    cout << so.rangeAddQueries(3, q) << endl;
    return 0;
}
