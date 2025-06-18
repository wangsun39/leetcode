#include "lc_pub.h"

class Solution {
    public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        ranges::sort(nums);
        int n=nums.size();
        int m=n/3;
        for (int i=0;i<m;i++) {
            if (nums[(i+1)*3-1]-nums[i*3]>k)
                return vector<vector<int>>{};
        }
        vector<vector<int>> ans(m,vector<int>(3));
        for (int i=0;i<n;i++) {
            ans[i/3][i%3]=nums[i];
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,3,4,8,7,9,3,5,1};

    Solution so;
    cout << so.divideArray(nums, 2) << endl;
    return 0;
}
