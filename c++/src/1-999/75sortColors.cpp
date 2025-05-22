#include "lc_pub.h"

class Solution {
    public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int c0=0,c1=0,c2=0;
        for (auto x: nums)
            if (x==0)c0++;
            else if(x==1) c1++;
            else c2++;
        for (int i=0;i<c0;i++) nums[i]=0;
        for (int i=c0;i<c0+c1;i++) nums[i]=1;
        for (int i=c1+c0;i<n;i++) nums[i]=2;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    return 0;
}
