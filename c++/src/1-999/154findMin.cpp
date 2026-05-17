#include "lc_pub.h"

class Solution {
public:
    int findMin(vector<int>& nums) {
        int n=nums.size();
        int l=0,r=n-1;
        int ans=nums[0];
        while (l < r - 1) {
            int mid=(l+r)/2;
            if (nums[l] < nums[r]) {
                return nums[l];
            }
            if (nums[l]<nums[mid]) {
                l=mid;
            }
            else if(nums[mid]<nums[r]) {
                r=mid;
            }
            // nums[l]>=nums[mid]>=nums[r]
            else if (nums[l]==nums[r]) {
                r--;
            }
            else if (nums[l]== nums[mid]) {
                l=mid;
            }
            else {
                r=mid;
            }
        }
        return min(nums[l],nums[r]);
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int>ratings{1,3,4,5,2};

    Solution so;
    auto v = so.candy(ratings);
    // auto v = so.minCut("ababababababababababababcbabababababababababababa");
    cout << v << endl;
    return 0;
}
