// 给你一个长度为 n 的整数数组 nums 和一个整数 k。

// 在一次操作中，你可以选择 nums 中的任意一个元素，并以任意顺序重新排列其十进制数字，组成一个新的整数。

// 返回在执行至多 k 次操作后，数组元素之和的最大值。

 

// 示例 1：

// 输入： nums = [123,45], k = 1

// 输出： 366

// 解释：

// 选择 nums[0] = 123，重新排列其数字，得到 321。
// 数组变为 [321, 45]。因此，元素之和为 321 + 45 = 366。
// 示例 2：

// 输入： nums = [102,90,14], k = 2

// 输出： 341

// 解释：

// 选择 nums[0] = 102，重新排列其数字，得到 210。
// 选择 nums[2] = 14，重新排列其数字，得到 41。
// 数组变为 [210, 90, 41]。因此，元素之和为 210 + 90 + 41 = 341。
 

// 提示：

// 1 <= n == nums.length <= 105
// 1 <= nums[i] <= 109
// 1 <= k <= n


#include "lc_pub.h"

class Solution {
public:
    long long maximizeSum(vector<int>& nums, int k) {
        long long ans=0;
        int n=nums.size();
        for (int i=0;i<n;i++) ans+=nums[i];
        vector<int> diff(n,0);
        for (int i=0;i<n;i++) {
            int a=nums[i];
            vector<int> di;
            while (a) {
                di.push_back(a%10);
                // b=b*10+a%10;
                a/=10;
            }
            ranges::sort(di, greater<int>{});
            int b=0;
            for (int x: di) {
                b=b*10+x;
            }
            diff[i]=b-nums[i];
        }
        ranges::sort(diff, greater<int>{});
        for (int i=0;i<k;i++) {
            ans+=diff[i];
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{-58,4,24,23};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");
    Solution so;

    return 0;
}
