#include "lc_pub.h"

class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int n=points.size();
        int ans=0;
        for (int i=0;i<n-1;i++) {
            int x=points[i][0],y=points[i][1];
            int u=points[i+1][0],v=points[i+1][1];
            int d1=abs(x-u),d2=abs(y-v);
            ans+=min(d1,d2)+abs(d1-d2);
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,6,5,1,8};
    Solution so;
    return 0;
}