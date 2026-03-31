// 给你一个整数 num。

// 如果一个数 num 的每一个 前缀 和每一个 后缀 都是 质数，则称该数为 完全质数。

// 如果 num 是完全质数，返回 true，否则返回 false。

// 注意：

// 一个数的 前缀 是由该数的 前 k 位数字构成的。
// 一个数的 后缀 是由该数的 后 k 位数字构成的。
// 质数 是大于 1 且只有两个因子（1 和它本身）的自然数。
// 个位数只有在它是 质数 时才被视为完全质数。
 

// 示例 1：

// 输入：num = 23

// 输出：true

// 解释：

// num = 23 的前缀是 2 和 23，它们都是质数。
// num = 23 的后缀是 3 和 23，它们都是质数。
// 所有的前缀和后缀都是质数，所以 23 是完全质数，答案是 true。
// 示例 2：

// 输入：num = 39

// 输出：false

// 解释：

// num = 39 的前缀是 3 和 39。3 是质数，但 39 不是质数。
// num = 39 的后缀是 9 和 39。9 和 39 都不是质数。
// 至少有一个前缀或后缀不是质数，所以 39 不是完全质数，答案是 false。
// 示例 3：

// 输入：num = 7

// 输出：true

// 解释：

// 7 是质数，所以它的所有前缀和后缀都是质数，答案是 true。
 

// 提示：

// 1 <= num <= 109

#include "lc_pub.h"

class Solution {
public:
    bool completePrime(int num) {
        vector<int> arr1,arr2;
        while (num) {
            arr1.insert(arr1.begin(), num%10);
            arr2.push_back(num%10);
            num/=10;
        }
        auto check=[&](int cur) {
            for (int y=2;y*y<=cur;y++) {
                if (cur % y == 0) return false;
            }
            return true;
        };
        if (arr1[0]==1||arr2[0]==1) return false;
        int x=0;
        for (auto y: arr1) {
            x=x*10+y;
            if (!check(x)) return false;
        }
        x=1;
        int y=0;
        for (int i=0;i<arr2.size();i++) {
            y=arr2[i]*x+y;
            if (!check(y)) return false;
            x*=10;
        }
        return true;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    cout<<so.completePrime(73)<<endl;
    return 0;
}
