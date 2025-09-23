#include "lc_pub.h"

class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int R=mat.size(),C=mat[0].size();
        if (R * C != r * c) return mat;
        std::vector<std::vector<int>> ans(r, std::vector<int>(c, 0));
        int x=0,y=0;
        for (int i=0;i<R;i++) {
            for (int j=0;j<C;j++) {
                ans[x][y]=mat[i][j];
                if (y<c-1) y++;
                else x++,y=0;
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
