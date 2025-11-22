#include "lc_pub.h"


class Solution {
    public:
    int minimumOperations(vector<int>& nums) {
        int ans=0;
        for (int x: nums) {
            ans += x % 3 != 0;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{2,1,4,3,1,1,1,5};

    Solution so;
    cout << so.minimumOperations(nums) << endl;
    return 0;
}
