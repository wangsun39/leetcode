#include "lc_pub.h"


class Solution {
    
    public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        int r=mat.size(),c=mat[0].size();
        vector<vector<int>> s(r+1,vector<int>(c+1, 0));
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                s[i+1][j+1]=s[i][j+1]+s[i+1][j]-s[i][j]+mat[i][j];
            }
        }
        int ans=0;
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                for (int k=ans+1;k<=min(r,c);k++) {
                    if (i+k-1>=r||j+k-1>=c) break;
                    if (s[i+k][j+k]-s[i+k][j]-s[i][j+k]+s[i][j]<=threshold)
                        ans=k;
                    else
                        break;
                }
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    auto mat=parseGrid("[[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]]");
    Solution so;
    cout<<so.maxSideLength(mat, 40184);

    return 0;
}
