#include "lc_pub.h"

class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int r=grid.size(),c=grid[0].size();
        vector<vector<int>> row(r+1,vector<int>(c+1, 0));
        vector<vector<int>> col(r+1,vector<int>(c+1, 0));
        vector<vector<int>> diag(r+1,vector<int>(c+1, 0));
        vector<vector<int>> anti(r+1,vector<int>(c+1, 0));

        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                row[i][j+1]=row[i][j]+grid[i][j];
                col[i+1][j]=col[i][j]+grid[i][j];
                diag[i+1][j+1]=diag[i][j]+grid[i][j];
                anti[i+1][j]=anti[i][j+1]+grid[i][j];
            }
        }
        for (int k=min(r,c);k>0;k--) {
            for (int i=k;i<=r;i++) {
                for (int j=k;j<=c;j++) {
                    // [i-k,i-1] * [j-k,j-1]
                    if (k==3&&i==4&&j==4)
                        cout<<1<<endl;
                    int s=diag[i][j]-diag[i-k][j-k];
                    if (s!=anti[i][j-k]-anti[i-k][j]) continue;

                    bool match=true;
                    for (int t=i-k;t<i;t++) {
                        if (row[t][j]-row[t][j-k]!=s) {
                            match=false;
                            break;
                        }
                    }
                    if (!match) continue;
                    for (int t=j-k;t<j;t++) {
                        if (col[i][t]-col[i-k][t]!=s) {
                            match=false;
                            break;
                        }
                    }
                    if (match) return k;
                }
            }
        }
        return 0;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,3};
    auto grid = parseGrid("[[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]");

    Solution so;
    cout<<so.largestMagicSquare(grid)<<endl;
    
    return 0;
}
