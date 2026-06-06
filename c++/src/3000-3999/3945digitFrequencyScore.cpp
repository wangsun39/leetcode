// 给你一个整数 n。

// n 的 得分 定义为：对所有 不同 数字 d，计算 d * freq(d) 的总和，其中 freq(d) 表示数字 d 在 n 中出现的次数。

// 返回一个整数，表示 n 的得分。

 

// 示例 1：

// 输入： n = 122

// 输出： 5

// 解释：

// 数字 1 出现 1 次，贡献为 1 * 1 = 1。
// 数字 2 出现 2 次，贡献为 2 * 2 = 4。
// 因此，n 的得分为 1 + 4 = 5。
// 示例 2：

// 输入： n = 101

// 输出： 2

// 解释：

// 数字 0 出现 1 次，贡献为 0 * 1 = 0。
// 数字 1 出现 2 次，贡献为 1 * 2 = 2。
// 因此，n 的得分为 2。
 

// 提示：

// 1 <= n <= 109

#include "lc_pub.h"

class Solution {
public:
    int digitFrequencyScore(int n) {
        int f[10]={0};
        while (n) {
            f[n%10]++;
            n/=10;
        }
        int ans=0;
        for (int i=0;i<10;i++) ans+=i*f[i];
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{73,92,31,78,89};
    // auto items=parseGrid("[[6,2],[2,6],[3,4]]");
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
