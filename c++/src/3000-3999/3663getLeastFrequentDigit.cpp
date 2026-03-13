// 给你一个整数 n，找出在其十进制表示中出现频率 最低 的数字。如果多个数字的出现频率相同，则选择 最小 的那个数字。

// 以整数形式返回所选的数字。

// 数字 x 的出现频率是指它在 n 的十进制表示中的出现次数。

 

// 示例 1:

// 输入： n = 1553322

// 输出： 1

// 解释：

// 在 n 中，出现频率最低的数字是 1，它只出现了一次。所有其他数字都出现了两次。

// 示例 2:

// 输入： n = 723344511

// 输出： 2

// 解释：

// 在 n 中，出现频率最低的数字是 7、2 和 5，它们都只出现了一次。

 

// 提示:

// 1 <= n <= 231 - 1

#include "lc_pub.h"


class Solution {
    public:
    int getLeastFrequentDigit(int n) {
        int cnt[10]={0};
        while (n) {
            int q=n/10;
            int r=n%10;
            cnt[r]++;
            n=q;
        }
        int ans,mn=100;
        for (int i=0;i<10;i++) {
            if (mn>cnt[i]&&cnt[i]) {
                ans=i;
                mn=cnt[i];
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>>q= parseGrid("[[0,0],[1,0],[0,1],[1,1]]");

    Solution so;
    return 0;
}
