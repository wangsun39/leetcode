// 给你一个整数数组 nums。

// 每个 nums[i] 都是一个 编码后的 整数，表示两个正整数 xi 和 yi。要解码 nums[i]，定义：

// widthi = nums[i] % 10。
// di = floor(nums[i] / 10)。
// xi 为由 di 的十进制表示中前 widthi 位数字组成的整数。
// yi 为由 di 的十进制表示中剩余所有数字组成的整数。
// 保证 di 的十进制表示包含的数字位数大于 widthi。因此，xi 和 yi 都至少包含一位数字。

// nums[i] 的 解码值 为 xiyi。

// 返回 nums 中所有元素的解码值之和，并对 109 + 7 取模。

// floor() 函数返回除法结果的整数部分。

 

// 示例 1：

// 输入： nums = [231]

// 输出： 8

// 解释：

// 对于 231，有 width = 1、d = 23、x = 2、y = 3。
// 231 的解码值为 23 = 8。
// 由于 nums 中只有一个元素，因此所有解码值之和为 8。
// 示例 2：

// 输入： nums = [2522,2101]

// 输出： 1649

// 解释：

// 对于 2522，有 width = 2、d = 252、x = 25、y = 2。
// 2522 的解码值为 252 = 625。
// 对于 2101，有 width = 1、d = 210、x = 2、y = 10。
// 2101 的解码值为 210 = 1024。
// 所有解码值之和为 625 + 1024 = 1649。
// 示例 3：

// 输入： nums = [2301]

// 输出： 73741817

// 解释：

// 对于 2301，有 width = 1、d = 230、x = 2、y = 30。
// 其解码值为 230 = 1073741824。
// 因此，答案为 1073741824 modulo (109 + 7) = 73741817。
 

// 提示：

// 1 <= nums.length <= 105
// 100 < nums[i] < 1015
// 1 <= widthi <= 9
// 1 <= xi, yi < 109
// 用于构成 xi 和 yi 的数字序列均不包含前导零。
// 保证 nums 中的每个元素都是有效的编码整数。

#include "lc_pub.h"

// 快速幂
long long mod_pow(long long b, long long n, long long MOD) {
    long long result = 1;
    b %= MOD;
    while (n > 0) {
        if (n & 1) {
            result = (result * b) % MOD;
        }
        b = (b * b) % MOD;
        n >>= 1;
    }
    return result;
}

class Solution {
public:
    int sumDecoded(vector<long long>& nums) {
        int MOD=1e9+7;
        
        auto calc = [&](long long x) -> int {
            int w=x%10;
            long long d=x/10;
            long long dd=d;
            vector<int> dig;
            while (dd) {
                dig.insert(dig.begin(), dd%10);
                dd/=10;
            }
            long long xi=0,yi=0;
            for (int i=0;i<w;i++) {
                xi=xi*10+dig[i];
            }
            for (int i=w;i<dig.size();i++) {
                yi=yi*10+dig[i];
            }
            long long res=pow(xi,yi);
            res%=MOD;
            
            return res;
        };

        long long ans=0;
        for (long long x: nums) {
            ans+=calc(x);
            ans%=MOD;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<long long> nums{4910362167};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    cout<<so.sumDecoded(nums);
    return 0;
}
