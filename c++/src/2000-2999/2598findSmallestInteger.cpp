#include "lc_pub.h"

class Solution {
    public:
    int findSmallestInteger(vector<int>& nums, int value) {
        int n=nums.size();
        for (int i=0;i<n;i++) {
            nums[i]=nums[i]%value;
            if (nums[i]<0) nums[i]+=value;
        }
        ranges::sort(nums);
        int cur=nums[0];
        for (int i=1;i<n;i++) {
            if (cur==nums[i]) nums[i]=nums[i-1]+value;
            else cur=nums[i];
        }
        ranges::sort(nums);
        for (int i=0;i<n;i++) {
            if (i!=nums[i]) return i;
        }
        return n;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,-10,7,13,6,8};

    Solution so;
    cout << so.findSmallestInteger(arr,7) << endl;
    return 0;
}
