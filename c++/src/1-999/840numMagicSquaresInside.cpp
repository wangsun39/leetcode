#include "lc_pub.h"

using namespace std;

class Solution {
    public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int row=grid.size(),col=grid[0].size();
        auto check=[&](int r, int c) -> bool {
            unordered_set<int> us;
            for (int i=0;i<3;i++) {
                for (int j=0;j<3;j++) {
                    us.insert(grid[r+i][c+j]);
                }
            }
            if (us.size()!=9) return false;
            int mx=ranges::max(us), mn=ranges::min(us);
            if (mx!=9||mn!=1) return false;
            int s=grid[r][c]+grid[r+1][c]+grid[r+2][c];
            for (int i=r;i<r+3;i++) {
                if (s!=grid[i][c]+grid[i][c+1]+grid[i][c+2]) return false;
            }
            for (int i=c;i<c+3;i++) {
                if (s!=grid[r][i]+grid[r+1][i]+grid[r+2][i]) return false;
            }
            if (s!=grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2]) return false;
            if (s!=grid[r+2][c]+grid[r+1][c+1]+grid[r][c+2]) return false;
            return true;
        };
        int ans=0;
        for (int i=0;i<row-2;i++) {
            for (int j=0;j<col-2;j++) {
                if (check(i, j)) ans++;
            }
        }
        return ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays = {1,1,2};
    Solution so;
    return 0;
}