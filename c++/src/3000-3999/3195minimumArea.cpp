#include "lc_pub.h"


class Solution {
    public:
    int minimumArea(vector<vector<int>>& grid) {
        int r=grid.size(),c=grid[0].size();
        int u=r,d=0,l=c,ri=0;
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++)
                if (grid[i][j]) {
                    u=min(u,i);d=max(d,i);l=min(l,j);ri=max(ri,j);
                }
        }
        return (d-u+1)*(ri-l+1);
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,3,3};

    Solution so;
    return 0;
}
