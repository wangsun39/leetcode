// 给你两个长度均为 n 的整数数组 nums 和 target。

// 对于每个下标 i，考虑将原数组的 后缀 nums[i..n - 1] 按 非递增顺序 排序。

// 返回使排序后的数组等于 target 的下标 i 的数量。

// 数组的 后缀 是从任意下标开始并延伸至数组末尾的 子数组。

 

// 示例 1：

// 输入： nums = [1,2,3], target = [3,2,1]

// 输出： 1

// 解释：

// i = 0：排序后的数组为 [3, 2, 1]，等于 target。
// i = 1：排序后的数组为 [1, 3, 2]。
// i = 2：排序后的数组为 [1, 2, 3]。
// 只有 i = 0 符合要求，因此答案为 1。

// 示例 2：

// 输入： nums = [1,5,6,4,6], target = [1,5,6,6,4]

// 输出： 2

// 解释：

// 选择 i = 2 或 i = 3，排序后都会得到 [1, 5, 6, 6, 4]。其他下标均无法得到 target。因此，答案为 2。

// 示例 3：

// 输入： nums = [7,6,8], target = [8,6,7]

// 输出： 0

// 解释：

// 分别对从下标 0、1 和 2 开始的后缀排序，会依次得到 [8, 7, 6]、[7, 8, 6] 和 [7, 6, 8]。它们均不等于 target，因此答案为 0。

 

// 提示：

// 1 <= n == nums.length == target.length <= 105
// 1 <= nums[i], target[i] <= 105​​​​​​​​​​​​​​



#include "lc_pub.h"

class Solution {
public:
    int countSuffix(vector<int>& nums, vector<int>& target) {
        int n=nums.size();
        int pre=-1;
        for (int i=0;i<n;i++) {
            if (nums[i]!=target[i]) break;
            pre=i;
        }
        unordered_map<int,int>diff;  // nums比target多的元素
        int ans=0;
        int d=0;  //  diff 中非0元素个数
        for (int i=n-1;i>=0;i--) {
            if (i<n-1 && target[i]<target[i+1]) break;
            diff[nums[i]]++;
            if (diff[nums[i]]==1) d++;
            diff[target[i]]--;
            if (diff[target[i]]==0) {
                d--;
            }
            if (d==0&&i-1<=pre) ans++;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3},t={3,2,1};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");
    Solution so;
    cout<<so.countSuffix(nums,t)<<endl;

    return 0;
}
