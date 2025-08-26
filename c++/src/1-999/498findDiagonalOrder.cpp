#include "lc_pub.h"

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int r= mat.size(), c=mat[0].size();
        vector<int> ans;
        int dir=0;
        for (int i=0;i<r+c;i++) {
            int x0,y0,xn,yn;
            if (dir==0) {
                x0=min(i, r-1);
                y0=i-x0;
            }
            else {
                y0=min(i, c-1);
                x0=i-y0;
            }
            for (int j=0;j<=i;j++) {
                int x,y;
                if (dir==0) x=x0-j,y=y0+j;
                else x=x0+j,y=y0-j;
                if (0<=x&&x<r&&0<=y&&y<c) 
                    ans.push_back(mat[x][y]);
                else
                    break;
            }
            dir=1-dir;
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[1,2,3],[4,5,6],[7,8,9]]");
    Solution so;
    auto v = so.findDiagonalOrder(arr);
    cout << v << endl;
    return 0;
}
