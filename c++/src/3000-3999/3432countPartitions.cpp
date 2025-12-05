#include "lc_pub.h"


class Solution {
    public:
    int countPartitions(vector<int>& nums) {
        int s=reduce(nums.begin(), nums.end());
        int n=nums.size();
        if (s&1) return 0;
        return n-1;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,4};

    Solution so;
    cout << so.countPartitions(nums) << endl;
    return 0;
}
