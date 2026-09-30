// 给你两个整数数组 source 和 target。

// 在一次 操作 中，你可以选择 source 中两个 不同 的下标 i 和 j，以及任何整数 delta。然后按如下方式更新 source：

// source[i] = source[i] + source[j] - delta
// source[j] = delta
// 如果在执行该操作 任意 次（包括零次）后能够使 source 等于 target，则返回 true。否则，返回 false。

 

// 示例 1：

// 输入： source = [1,2,3], target = [0,2,4]

// 输出： true

// 解释：

// 选择下标 i = 0 和 j = 2，并设置 delta = 4。
// 操作前，source[0] = 1 且 source[2] = 3。
// 操作后，
// source[0] = 1 + 3 - 4 = 0
// source[2] = 4
// 因此，source 变为 [0, 2, 4]，这与 target 相等。
// 因此，答案为 true。
// 示例 2：

// 输入： source = [-5,-5], target = [-15,5]

// 输出： true

// 解释：

// 选择下标 i = 1 和 j = 0，并设置 delta = -15。
// 操作前，source[1] = -5 且 source[0] = -5。
// 操作后，
// source[1] = -5 + (-5) - (-15) = 5
// source[0] = -15
// 因此，source 变为 [-15, 5]，这与 target 相等。
// 因此，答案为 true。
// 示例 3：

// 输入： source = [1,2,1], target = [0,2,5]

// 输出： false

// 解释：

// 可以证明，无论执行什么操作，都无法使 source 等于 target。因此，答案为 false。

 

// 提示：

// 2 <= source.length == target.length <= 105
// -109 <= source[i], target[i] <= 109

#include "lc_pub.h"

class Solution {
public:
    bool canTransform(vector<int>& source, vector<int>& target) {
        long long a=reduce(source.begin(), source.end(), 0LL);
        long long b=reduce(target.begin(), target.end(), 0LL);
        return a==b;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-10,-21,-7};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
