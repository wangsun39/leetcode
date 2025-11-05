#include "lc_pub.h"

class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int n = colors.size();
        int mx = neededTime[0],s=neededTime[0];
        int ans = 0;
        for (int i=0;i<n-1;i++) {
            if (colors[i]==colors[i+1]) {
                s+=neededTime[i+1];
                mx=max(mx, neededTime[i+1]);
            }
            else {
                ans+=s-mx;
                mx=s=neededTime[i+1];
            }
        }
        return ans+s-mx;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> p = {1,2,3,4,7};
    Solution so;
    return 0;
}
