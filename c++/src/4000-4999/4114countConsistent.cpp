// 给你一个整数数组 nums。

// 如果一个子数组中所有元素的 按位与 运算结果等于该子数组的 最小值 ，则称该子数组为 一致子数组 。

// 返回 nums 中 一致子数组 的个数。

// 子数组 是数组中一个连续、非空的元素序列。

 

// 示例 1：

// 输入： nums = [5,3,1,2]

// 输出： 6

// 解释：

// 以下子数组是一致子数组：

// 子数组	包含的值	按位与	最小值
// nums[0..0]	[5]	5	5
// nums[1..1]	[3]	3	3
// nums[2..2]	[1]	1	1
// nums[3..3]	[2]	2	2
// nums[1..2]	[3, 1]	3 & 1 = 1	1
// nums[0..2]	[5, 3, 1]	5 & 3 & 1 = 1	1
// 因此，一致子数组的个数为 6。

// 示例 2：

// 输入： nums = [1,1,1]

// 输出： 6

// 解释：

// 对于每个子数组，其按位与运算结果和最小值均等于 1。因此，答案为 6。

// 示例 3：

// 输入： nums = [0]

// 输出： 1

// 解释：

// 唯一的子数组是 [0]，其按位与运算结果和最小值均为 0。因此，答案为 1。

 

// 提示：

// 1 <= nums.length <= 2 * 105
// 0 <= nums[i] <= 106


#include "lc_pub.h"

class Solution {
public:
    long long countConsistent(vector<int>& nums) {
        int n=nums.size();
        vector<int>right(n, 0);  // nums[i] 向右最多能覆盖到的长度
        stack<int> st;
        for (int i=n-1;i>=0;i--) {
            while (st.size()&&(nums[st.top()]&nums[i])==nums[i]) {
                if (nums[st.top()]==nums[i]) break;
                st.pop();
            }
            if (st.size())
                right[i]=st.top()-i;
            else
                right[i]=n-i;
            st.push(i);
        }
        st = stack<int>();
        long long ans=0;
        for (int i=0;i<n;i++) {
            while (st.size()&&(nums[st.top()]&nums[i])==nums[i]) {
                st.pop();
            }
            if (st.size()) {
                int l=i-st.top();
                ans+=(long long)l*right[i];
            }
            else {
                int l=i+1;
                ans+=(long long)l*right[i];
            }

            st.push(i);
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums = {5, 3, 1, 2};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");
    Solution so;
    cout<<so.countConsistent(nums)<<endl;

    return 0;
}
