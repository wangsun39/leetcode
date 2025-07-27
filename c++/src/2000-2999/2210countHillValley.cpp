#include "lc_pub.h"


class Solution {
public:
    int countHillValley(vector<int>& nums) {
        int n=nums.size(), ans=0;
        vector<int>left(n,0),right(n,0);
        for (int i=1;i<n-1;i++) {
            if (nums[i-1]<nums[i]) {
                left[i]=1;
            }
            else if (nums[i-1]>nums[i]) {
                left[i]=2;
            }
            else {
                left[i]=left[i-1];
            }
        }
        for (int i=n-2;i>=0;i--) {
            if (nums[i]<nums[i+1]) {
                right[i]=2;
            }
            else if (nums[i]>nums[i+1]) {
                right[i]=1;
            }
            else {
                right[i]=right[i+1];
            }
        }
        for (int i=1;i<n-1;i++) {
            if (left[i]==right[i]&&left[i]&&nums[i-1]!=nums[i])
                ans++;
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr = parseGrid("[[3,2],[4,3],[4,4],[2,5]]");
    vector<int> n1{2,4,1,1,6,5}, n2{0,1,2,3};

    Solution so;
    cout << so.countHillValley(n1) << endl;
    return 0;
}
