#include "lc_pub.h"

using namespace std;

class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        ranges::sort(nums);
        int n = nums.size();
        int ans=0;
        for (int i=0;i<n;i++) {
            if (nums[i] == 0) continue;
            int r=i+2;
            for (int l=i+1;l<n;l++) {
                while (r < n&&nums[i]+nums[l]>nums[r]) {
                    r++;
                }
                ans+=max(0,r-l-1);
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{0,0,0};
    Solution so;
    cout << so.triangleNumber(nums) <<endl;
    return 0;
}