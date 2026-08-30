// 给你一个整数数组 nums 和一个整数 sum。

// 一次 操作 中，选择一个当前值为 x 的元素，并将其替换为 2 * x 或 floor(x / 2)。

// 对于每个元素，对其执行的所有 乘法 操作都必须发生在任何 除法 操作之前。

// 返回所需的 最少 操作次数，使得操作后的数组中存在一个 子集，其元素之和 恰好 等于 sum。如果无法做到，则返回 -1。

// 数组的 子集 是从数组中选择若干个元素得到的集合，也可以不选择任何元素。

// floor() 函数返回除法结果的整数部分。

 

// 示例 1：

// 输入： nums = [5,6,10], sum = 4

// 输出： 3

// 解释：

// 将 nums[0] = 5 连续除以 2 两次：5 → 2 → 1，需要 2 次操作。
// 将 nums[1] = 6 除以 2 一次：6 → 3，需要 1 次操作。
// 执行这些操作后，nums = [1, 3, 10]。子集 {1, 3} 的元素和为 4，总共使用了 3 次操作。
// 示例 2：

// 输入： nums = [10,2], sum = 13

// 输出： 3

// 解释：

// 将 nums[0] = 10 除以 2 一次：10 → 5，需要 1 次操作。
// 将 nums[1] = 2 连续乘以 2 两次：2 → 4 → 8，需要 2 次操作。
// 执行这些操作后，nums = [5, 8]。子集 {5, 8} 的元素和为 13，总共使用了 3 次操作。
// 示例 3：

// 输入： nums = [6,3], sum = 8

// 输出： -1

// 解释：

// 不存在任何操作序列，能够使 nums 的某个子集的元素和等于 8，因此答案为 -1。
 

// 提示：

// 1 <= nums.length <= 100
// 1 <= nums[i] <= 500
// 1 <= sum <= 5000

#include "lc_pub.h"

const int MX = 5001;
vector<unordered_map<int,int>>  mps(MX, unordered_map<int,int>());   // mps[i][j]  表示从i变成j的最少操作次数

auto init = [] {
    for (int i=1;i<MX;i++) {
        int c=0;
        int j=i;
        while (j < MX) {
            // 对每个i不断乘以2
            mps[i][j]=c;
            j*=2;
            c++;
        }
        c=1;
        j=i>>1;
        while (j > 0) {
            // j 为每个 i/(2^m)
            if (mps[i].find(j) != mps[i].end()&&mps[i][j]<=c) {
                j>>=1;
                c++;
                continue;
            }
            mps[i][j]=c;

            j >>= 1;
            c++;
        }
    }
    return 0;
}();

class Solution {
public:
    int minOperations(vector<int>& nums, int sum) {
        int n=nums.size();
        vector<vector<int>> dp(n, vector<int>(sum+1, INT_MAX));  // 前i个数构成j的最小操作次数
        for (auto &[k, v]: mps[nums[0]]) {
            if (k<=sum)
                dp[0][k]=v;
        }

        for (int i=1;i<n;i++) {
            int x=nums[i];
            for (int j=1;j<sum+1;j++) {
                dp[i][j]=dp[i-1][j];
                for (auto &[k, v]: mps[x]) {
                    if (k > j) continue;
                    if (k == j) {
                        dp[i][j]=min(dp[i][j], v);
                        continue;
                    }
                    if (dp[i-1][j-k] < INT_MAX) {
                        dp[i][j]=min(dp[i][j], dp[i-1][j-k]+v);
                    }
                }
            }
        }

        if (dp[n-1][sum]==INT_MAX) return -1;
        return dp[n-1][sum];

    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{499,499,499};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.minOperations(nums, 5000);
    return 0;
}
