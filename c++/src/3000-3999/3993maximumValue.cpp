// 给你三个整数 n、s 和 m。

// 如果一个长度为 n 的整数序列 seq 满足以下条件，则认为它是 有效 的：

// seq[0] = s。
// 序列是 交替 的，这意味着：
// seq[0] > seq[1] < seq[2] > ...，或者
// seq[0] < seq[1] > seq[2] < ...。
// 对于每个相邻元素对，|seq[i] - seq[i - 1]| <= m。
// 长度为 1 的序列被认为是交替的。

// 返回任何有效序列中可能出现的 最大 元素。

 

// 示例 1：

// 输入： n = 4, s = 3, m = 5

// 输出： 12

// 解释：

// 一个有效的序列是 [3, 8, 7, 12]。
// 序列中的最大元素是 12。
// 示例 2：

// 输入： n = 2, s = 4, m = 3

// 输出： 7

// 解释：

// 一个有效的序列是 [4, 7]。
// 序列中的最大元素是 7。
 

// 提示：

// 1 <= n, s <= 109
// 1 <= m <= 105

#include "lc_pub.h"

class Solution {
public:
    long long maximumValue(int n, int s, int m) {
        int n1=(n)/2,n2=(n-1)/2;
        long long ans=0;
        if (n1>n2||n1==0)
            ans+=s+(long long)n1*m-n2;
        else
            ans+=s+(long long)n1*m-n2+1;
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{0,0,0,2,0};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
