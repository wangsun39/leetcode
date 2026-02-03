#include "lc_pub.h"


class Solution {
    public:
    bool isTrionic(vector<int>& nums) {
        int n=nums.size();
        int p1=0,p2=0;
        for (int i=1;i<n-1;i++) {
            if (nums[i-1]==nums[i]||nums[i]==nums[i+1]) return false;
            if (nums[i-1]<nums[i]&&nums[i]>nums[i+1]) {
                if (p1) return false;
                p1=i;
            }
            if (nums[i-1]>nums[i]&&nums[i]<nums[i+1]) {
                if (!p1||p2) return false;
                p2=i;
            }
        }
        return p1&&p2;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>>q= parseGrid("[[0,0],[1,0],[0,1],[1,1]]");

    Solution so;
    return 0;
}
