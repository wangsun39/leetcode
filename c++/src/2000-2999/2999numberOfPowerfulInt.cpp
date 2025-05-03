#include "lc_pub.h"

class Solution {
    public:
    long long numberOfPowerfulInt(long long start, long long finish, int limit, string s) {
        
        string low = to_string(start);
        string high = to_string(finish);
        int n = high.size();
        low = string(n - low.size(), '0') + low; // 补前导零，和 high 对齐
        int diff = n - s.size();

        vector<long long> memo(n, -1);
        // 在枚举完第 i 个数位能够填入的数字后，之后填入的数字并不会改变这个结果，因此我们可以使用记忆化的方法来避免重复计算。
        // 注意，对于受到 limitLow 或 limitHigh 约束的状态来说，它们只会被遍历到一次。这是因为如果当前位受到约束，那么前面的所有位都受到约束，这只有一种方案，所以我们只需要记忆化没有受到约束的状态即可。


        // auto dfs = [&](this auto&& dfs, int i, bool limit_low, bool limit_high) -> long long {
        std::function<long long(int, bool, bool)> dfs = [&](int i, bool limit_low, bool limit_high) -> long long {
            if (i == low.size()) {
                return 1;
            }

            if (!limit_low && !limit_high && memo[i] != -1) {
                return memo[i]; // 之前计算过
            }

            // 第 i 个数位可以从 lo 枚举到 hi
            // 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
            int lo = limit_low ? low[i] - '0' : 0;
            int hi = limit_high ? high[i] - '0' : 9;

            long long res = 0;
            if (i < diff) { // 枚举这个数位填什么
                for (int d = lo; d <= min(hi, limit); d++) {
                    res += dfs(i + 1, limit_low && d == lo, limit_high && d == hi);
                }
            } else { // 这个数位只能填 s[i-diff]
                int x = s[i - diff] - '0';
                if (lo <= x && x <= hi) { // 题目保证 x <= limit，无需判断
                    res = dfs(i + 1, limit_low && x == lo, limit_high && x == hi);
                }
            }

            if (!limit_low && !limit_high) {
                memo[i] = res; // 记忆化 (i,false,false)
            }
            return res;
        };
        return dfs(0, true, true);

    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{12,6,1,2,7};

    Solution so;
    cout << so.numberOfPowerfulInt(1,6000,4,"124") << endl;
    return 0;
}
