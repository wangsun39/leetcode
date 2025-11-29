#include "lc_pub.h"


class Solution {
    public:
    int minOperations(vector<int>& nums, int k) {
        int s=reduce(nums.begin(), nums.end(), 0);
        return s%k;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    cout<<so.minOperations(nums, 5)<<endl;
    return 0;
}
