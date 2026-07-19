

#include "lc_pub.h"

class Solution {
public:
    int minAdjacentSwaps(vector<int>& nums, int a, int b) {
        int n1=0,n2=0,n3=0,n=nums.size();
        int MOD=1E9+7;
        for (int i=0;i<n;i++) {
            if (nums[i]<a) n1++;
            else if (nums[i]>b) n3++;
            else n2++;
        }
        int g_a=0,g_b=0;  // 遍历过程中有多少个数比a大，以及有多少数比a大且比b小
        long long ans=0;
        // 先把应属于第一段的数都交换到第一段
        for (int i=0;i<n;i++) {
            if (nums[i]>=a) {
                g_a++;
            }
            else { // 第一段的数，要与所有g_a个数交换
                ans+=g_a;
                ans%=MOD;
            }
        }
        // 再把应属于第三段的数都交换到第三段
        for (int i=n-1;i>=0;i--) {
            if (nums[i]>=a&&nums[i]<=b) {
                g_b++;
            }
            else if (nums[i]>b) { // 第三段的数，要与所有g_b个数交换
                ans+=g_b;
                ans%=MOD;
            }
        }
        
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,3,2,4,5,6};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.minAdjacentSwaps(nums, 3,4);
    return 0;
}
