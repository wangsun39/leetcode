// 给你一个长度为 n 的整数数组 nums。

// 如果一对下标 (i, j) 满足以下所有条件，则称其为一个影子对 ：

// 0 <= i < j < n
// nums[i] < nums[j]
// 不存在 下标 k，使得 i < k < j 且 nums[k] < nums[i] < nums[j]。
// 返回 影子对 的总数。

 

// 示例 1：

// 输入： nums = [3,1,4,1,5]

// 输出： 3

// 解释：

// (i, j)	nums[i]	nums[j]	为何是影子对
// (1, 2)	1	4	不存在满足 1 < k < 2 的下标 k
// (1, 4)	1	5	nums[2] = 4 和 nums[3] = 1 都不小于 1
// (3, 4)	1	5	不存在满足 3 < k < 4 的下标 k
// 因此，答案为 3。

// 示例 2：

// 输入： nums = [6,7,6,6,7]

// 输出： 4

// 解释：

// (i, j)	nums[i]	nums[j]	为何是影子对
// (0, 1)	6	7	不存在满足 0 < k < 1 的下标 k
// (0, 4)	6	7	nums[1] = 7、nums[2] = 6 和 nums[3] = 6 都不小于 6
// (2, 4)	6	7	nums[3] = 6 不小于 6
// (3, 4)	6	7	不存在满足 3 < k < 4 的下标 k
// 因此，答案为 4。

// 示例 3：

// 输入： nums = [1,2,3,4]

// 输出： 6

// 解释：

// (i, j)	nums[i]	nums[j]	为何是影子对
// (0, 1)	1	2	不存在满足 0 < k < 1 的下标 k
// (0, 2)	1	3	nums[1] = 2 不小于 1
// (0, 3)	1	4	nums[1] = 2 和 nums[2] = 3 都不小于 1
// (1, 2)	2	3	不存在满足 1 < k < 2 的下标 k
// (1, 3)	2	4	nums[2] = 3 不小于 2
// (2, 3)	3	4	不存在满足 2 < k < 3 的下标 k
// 因此，答案为 6。

 

// 提示：

// 3 <= n == nums.length <= 105
// 1 <= nums[i] <= 109

#include "lc_pub.h"

class Solution {
public:
    long long shadowPairs(vector<int>& nums) {
        stack<int> st;
        int n=nums.size();
        vector<int> dp(n, 0);
        unordered_map<int,int>counter;
        for (int i=0;i<n;i++) {
            while (st.size()) {
                if (nums[st.top()]>=nums[i]) {
                    if (nums[st.top()]>nums[i])
                        counter[nums[st.top()]]=0;  // 为相等的数进行特殊处理
                    st.pop();
                }
                else
                    break;
            }
            // 找到最近的一个比nums[i]小的数
            if (st.size()) {
                dp[i]=dp[st.top()]+counter[nums[st.top()]];  // 前面与 nums[st.top()] 相等的数都能与 nums[i]构成数对
            }
            st.push(i);
            counter[nums[i]]++;
        }
        return reduce(dp.begin(), dp.end(), 0LL);
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{8,14,1,8,27,31};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.shadowPairs(nums)<<endl;
    return 0;
}
