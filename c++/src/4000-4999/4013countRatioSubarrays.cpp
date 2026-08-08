// 给你一个整数数组 nums。

// 选择 恰好一对 不同下标 i 和 j。该数对的 强度 定义为：

// (nums[i] * nums[j]) / gcd(nums[i], nums[j])2

// 返回所有可能数对中的 最大 强度。

// gcd(a, b) 表示 a 和 b 的 最大公约数 。

 

// 示例 1：

// 输入： nums = [2,3,5]

// 输出： 15

// 解释：

// 选择 i = 1 和 j = 2，得到强度：

// (3 * 5) / gcd(3, 5)2 = 15 / 1 = 15，这是所有数对中的最大值。

// 示例 2：

// 输入： nums = [4,6,8]

// 输出： 12

// 解释：

// 选择 i = 1 和 j = 2，得到强度：

// (6 * 8) / gcd(6, 8)2 = 48 / 4 = 12，这是所有数对中的最大值。

// 示例 3：

// 输入： nums = [3,3]

// 输出： 1

// 解释：

// 选择 i = 0 和 j = 1，得到强度：

// (3 * 3) / gcd(3, 3)2 = 9 / 9 = 1，这是唯一数对的强度。

 

// 提示：

// 2 <= nums.length <= 2000
// 1 <= nums[i] <= 105

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#include "lc_pub.h"

// 允许重复元素：用 pair 或自定义结构体
using ordered_set = tree<
    pair<long long, long long>,                     // 键值类型
    null_type,                          // 无映射
    std::less<pair<long long, long long>>,          // 比较函数
    rb_tree_tag,                        // 红黑树
    tree_order_statistics_node_update   // 支持 order_of_key
>;



class Solution {
public:
    long long countRatioSubarrays(vector<int>& nums, int a, int b) {
        int n=nums.size();
        long long o=0,e=0;

        ordered_set s;
        int counter = 0;
        
        auto insert = [&] (long long x) {
            s.insert({x, counter++});  // 第二个值保证唯一性
        };

        // 查询 >= x 的元素个数
        auto countGe = [&] (long long x) -> int {
            // 第一个 >= x 的元素位置 = 小于 x 的元素个数
            int lessThanX = s.order_of_key({x, INT_MIN});
            return s.size() - lessThanX;
        };

        insert(0);

        long long ans=0;
        for (int i=0;i<n;i++) {
            if (nums[i]&1) o++;
            else e++;
            long long f=b*e-a*o;
            int v=countGe(f);
            ans+=v;
            insert(f);
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{2950711,3747997,1250343};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.countRatioSubarrays(nums, 1000000000, 1);
    return 0;
}
