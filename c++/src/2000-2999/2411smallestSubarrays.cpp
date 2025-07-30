#include "lc_pub.h"

class Solution {
    public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, 1);
        for (int i=0;i<n;i++) {
            for (int j=i-1;j>=0;j--) {
                if ((nums[j]|nums[i])==nums[j]) break;
                nums[j]|=nums[i];
                ans[j]=i-j+1;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,0,2,1,3}, t{8,2,5,8};

    Solution so;
    cout << so.smallestSubarrays(arr) << endl;
    return 0;
}
