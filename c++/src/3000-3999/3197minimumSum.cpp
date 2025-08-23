#include "lc_pub.h"


class Solution {
    public:
    int minimumSum(vector<vector<int>>& grid) {
        int r=grid.size(),c=grid[0].size();
        auto calc = [&] (int a,int b,int c, int d) -> int {
            if (a>b||c>d) return 0;
            int up=b,down=a,l=d,ri=c;
            for (int i=a;i<=b;i++)
                for (int j=c;j<=d;j++)
                    if (grid[i][j]) {
                        up=min(up,i);down=max(down,i);l=min(l,j);ri=max(ri,j);
                    }
            return max((down-up+1)*(ri-l+1),0);
        };
        int ans=r*c;
        for (int i=0;i<r;i++) {
            int s1=calc(0,i,0,c-1);
            for (int j=i+1;j<r;j++) {
                int s2=calc(i+1,j,0,c-1);
                int s3=calc(j+1,r-1,0,c-1);
                ans=min(ans,s1+s2+s3);
            }
            for (int j=0;j<c;j++) {
                int s2=calc(i+1,r-1,0,j);
                int s3=calc(i+1,r-1,j+1,c-1);
                ans=min(ans,s1+s2+s3);
            }
            s1=calc(i+1,r-1,0,c-1);
            for (int j=0;j<c;j++) {
                ans=min(ans,s1+calc(0,i,0,j)+calc(0,i,j+1,c-1));
            }
        }
        for (int i=0;i<c;i++) {
            int s1=calc(0,r-1,0,i);
            for (int j=i+1;j<c;j++) {
                ans=min(ans,s1+calc(0,r-1,i+1,j)+calc(0,r-1,j+1,c-1));
            }
            for (int j=0;j<r;j++) {
                ans=min(ans,s1+calc(0,j,i+1,c-1)+calc(j+1,r-1,i+1,c-1));
            }
            s1=calc(0,r-1,i+1,c-1);
            for (int j=0;j<r;j++) {
                ans=min(ans,s1+calc(0,j,0,i)+calc(j+1,r-1,0,i));
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto nums=parseGrid("[[0,0,0],[0,0,0],[0,0,1],[1,1,0]]");

    Solution so;
    cout<<so.minimumSum(nums)<<endl;
    return 0;
}
