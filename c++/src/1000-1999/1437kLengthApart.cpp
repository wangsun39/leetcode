#include "lc_pub.h"

class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int pre=-k-1;
        for (int i=0;i<nums.size();i++) {
            if (nums[i]==1) {
                if (i-pre-1<k) return false;
                pre=i;
            }
        }
        return true;
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};
    
    Solution so;
    return 0;
}
