#include "lc_pub.h"

class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        int s=accumulate(nums.begin(), nums.end(), 0);
        int cur=0,n=nums.size();
        for (int i=1;i<n;i++) {
            cur+=i*nums[i];
        }
        int ans=cur;
        for (int i=0;i<n-1;i++) {
            cur-= s-n*nums[i];
            ans =max(ans,cur);
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3};
    Solution so;
    // auto v = so.lexicalOrder(22);
    // cout << v << endl;
    return 0;
}
