#include "lc_pub.h"

class Solution {
    public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        long long s1 = accumulate(nums1, 0);
        // long long s1 = accumulate(nums1.begin(), nums1.end(), 0LL);
        long long s2 = accumulate(nums2.begin(), nums2.end(), 0LL);
        int z1 = ranges::count(nums1, 0);
        int z2 = ranges::count(nums2, 0);
        if (s1 + z1 > s2 + z2)
            return z2 ? s1 + z1 : -1;
        if (s1 + z1 < s2 + z2)
            return z1 ? s2 + z2 : -1;
        return s1 + z1;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums1{3,2,0,1,0};
    vector<int> nums2{6,5,0};

    Solution so;
    cout << so.minSum(nums1, nums2) << endl;
    return 0;
}
