#include "lc_pub.h"

class Solution {
    
    public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int r=matrix.size(),c=matrix[0].size();
        vector<vector<int>> h(r, vector<int>(c, 0));  // matrix[i][j] 向上有多少个连续1
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                if (matrix[i][j] == 0) continue;
                if (i==0)
                    h[i][j]=1;
                else
                    h[i][j]=h[i-1][j]+1;
            }
        }
        int ans=0;

        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                if (h[i][j]==0) continue;
                int he=h[i][j];
                for (int k=j;k<c;k++) {
                    // 从 j 列 到 k 列
                    he=min(he,h[i][k]);
                    if (he==0) break;
                    ans=max(ans, he * (k - j + 1));
                }
            }
        }
        return ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}
