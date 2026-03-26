// 给你一个 正 整数 n。

// 令 s 为 n 的 二进制表示（不含前导零）。

// 二进制字符串 s 的 反转 是指将 s 中的字符按相反顺序排列得到的字符串。

// 你可以翻转 s 中的任意一位（将 0 → 1 或 1 → 0）。每次翻转 仅 影响一位。

// 请返回使 s 等于其原始形式的反转所需的 最少 翻转次数。

 

// 示例 1：

// 输入： n = 7

// 输出： 0

// 解释：

// 7 的二进制表示为 "111"。其反转也是 "111"，两者相同。因此，不需要翻转。

// 示例 2：

// 输入： n = 10

// 输出： 4

// 解释：

// 10 的二进制表示为 "1010"。其反转为 "0101"。必须翻转所有四位才能使它们相等。因此，所需的最少翻转次数为 4。

 

// 提示：

// 1 <= n <= 109

#include "lc_pub.h"

class Solution {
public:
    int minimumFlips(int n) {
        vector<int> arr;
        while (n) {
            arr.push_back(n & 1);
            n>>=1;
        }
        int ans=0,m=arr.size();
        for (int i=0;i<m;i++) {
            if (arr[i]!=arr[m-1-i]) ans++;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    return 0;
}
