#include "lc_pub.h"


class Solution {
    public:
    long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
        int n=bottomLeft.size();
        long long ans=0;
        for (int i=0;i<n;i++) {
            int x1=bottomLeft[i][0],x2=topRight[i][0],y1=bottomLeft[i][1],y2=topRight[i][1];
            for (int j=i+1;j<n;j++) {
                int x3=bottomLeft[j][0],x4=topRight[j][0],y3=bottomLeft[j][1],y4=topRight[j][1];
                int r1=min(x2,x4)-max(x1,x3);
                int r2=min(y2,y4)-max(y1,y3);
                if (r1<=0||r2<=0) continue;
                long long r=min(r1,r2);
                ans=max(ans,r*r);
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto points = parseGrid("[[1,1],[2,2],[3,3]]");

    Solution so;
    return 0;
}
