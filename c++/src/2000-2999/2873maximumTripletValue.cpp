#include "lc_pub.h"

class Solution {
    public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> left(n, 0), right(n, 0);
        long long ans = 0;
        for (int i=1;i<n;i++) {
            left[i]=max(left[i-1],nums[i-1]);  // i 左侧最大的数
        }
        for (int i=n-2;i>=0;i--) {
            right[i]=max(right[i+1],nums[i+1]);  // i 右侧最大的数
        }
        for (int i=1;i<n-1;i++) {
            ans = max(ans, (left[i]-nums[i])*(long long)right[i]);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{12,6,1,2,7};

    Solution so;
    cout << so.maximumTripletValue(nums) << endl;
    return 0;
}
