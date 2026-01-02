#include "lc_pub.h"

using namespace std;

class Solution {
    public:
    int repeatedNTimes(vector<int>& nums) {
        int n=nums.size();
        if (nums[0]==nums[1]||nums[0]==nums[n-1]) return nums[0];
        for (int i=2;i<n;i++) {
            if (nums[i-1]==nums[i]||nums[i-2]==nums[i]) return nums[i];
        }
        return 0;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}