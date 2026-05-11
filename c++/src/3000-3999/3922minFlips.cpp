// 给你一个二进制字符串 s。

// 如果一个字符串 不 包含 "011" 或 "110" 作为 子序列，则认为该字符串是 连贯的 。

// 返回一个整数，表示使 s 连贯所需的 最少 修改次数。

// 子序列 是指可以通过删除原字符串中的某些字符（或不删除任何字符）且不改变剩余字符顺序而得到的字符串。

 

// 示例 1：

// 输入： s = "1010"

// 输出： 1

// 解释：

// 翻转 s[0] 得到 "0010"，它不包含 "011" 或 "110" 子序列。

// 示例 2：

// 输入： s = "0110"

// 输出： 1

// 解释：

// 翻转 s[1] 得到 "0010"，移除了所有禁止的子序列 "011" 和 "110"。

// 示例 3：

// 输入： s = "1000"

// 输出： 0

// 解释：

// 该字符串已经不包含 "011" 或 "110" 子序列，因此不需要翻转。

 

// 提示：

// 1 <= s.length <= 105
// s[i] 是 '0' 或 '1'。

#include "lc_pub.h"

class Solution {
public:
    int minFlips(string s) {
        int n=s.size();
        if (n<=2) return 0;
        int c0=0;
        for (char c: s) if(c=='0')c0++;
        int ans=min(c0,n-c0-1);
        ans=max(ans,0);
        int x=0;  // 构造100...001，需要的操作次数
        if (s[0]=='0'){x++;c0--;}
        if (s[n-1]=='0'){x++;c0--;}
        x+=n-2-c0;
        return min(ans,x);

    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4};

    Solution so;
    return 0;
}
