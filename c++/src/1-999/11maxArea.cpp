#include "lc_pub.h"

class Solution {
public:
    int maxArea(vector<int>& height) {
        int n=height.size();
        vector<pair<int,int>> hi;
        for (int i=0;i<n;i++)
            hi.push_back({height[i],i});
        ranges::sort(hi);        
        int mx = hi[n-1].second;
        int mn = hi[n-1].second;
        int ans = 0;
        for (int i=n-2;i>=0;i--) {
            ans = max(ans, hi[i].first * abs(hi[i].second-mx));
            ans = max(ans, hi[i].first * abs(hi[i].second-mn));
            mx = max(mx, hi[i].second);
            mn = min(mn, hi[i].second);
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> nums = {4, 5, 6};
    Solution so;
    return 0;
}
