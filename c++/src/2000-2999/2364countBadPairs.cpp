#include "lc_pub.h"

class Solution {
    public:
    long long countBadPairs(vector<int>& nums) {
        unordered_map<int, int> counter;
        long long ans=0;
        for (int i=0;i<nums.size();i++) {
            ans += (i-counter[i-nums[i]]);
            counter[i-nums[i]]++;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {4,1,3,3};

    Solution so;
    cout << so.countBadPairs(arr) << endl;
    return 0;
}
