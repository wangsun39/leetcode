#include "lc_pub.h"


class Solution {
    public:
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        vector<int>r1(n,n+1),r2(n,0),c1(n,n+1),c2(n,0);
        int ans=0;
        for (auto & b: buildings) {
            c1[b[0]]=min(c1[b[0]], b[1]);
            c2[b[0]]=max(c2[b[0]], b[1]);
            r1[b[1]]=min(r1[b[1]], b[0]);
            r2[b[1]]=max(r2[b[1]], b[0]);
        }
        for (auto & b: buildings) {
            if (c1[b[0]]<b[1]&&b[1]<c2[b[0]]&&r1[b[1]]<b[0]&&b[0]<r2[b[1]])
                ans++;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    return 0;
}
