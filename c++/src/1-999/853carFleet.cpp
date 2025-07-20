#include "lc_pub.h"

class Solution {
    public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<vector<long long>> z(n, vector<long long>(2, 0));
        for (int i=0;i<n;i++) {
            z[i][0] = position[i];
            z[i][1] = speed[i];
        }
        ranges::sort(z);
        int ans=1;
        auto after = z[n-1];
        for (int i=n-2;i>=0;i--) {
            if (z[i][1]<=after[1]||after[1]*(target-z[i][0])>z[i][1]*(target-after[0])) {
                after=z[i];
                ans++;
            }
        }
        return ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> p = {10,8,0,5,3}, s{2,4,1,1,3};
    Solution so;
    cout<<so.carFleet(12,p,s)<<endl;
    return 0;
}