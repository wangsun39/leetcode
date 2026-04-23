// 给定一个由小写英文字母组成的字符串 s。

// 返回移除字符串 s 尾部 所有元音字母 后得到的字符串。

// 元音字母包括字符 'a'、'e'、'i'、'o' 和 'u'。

 

// 示例 1：

// 输入： s = "idea"

// 输出： "id"

// 解释：

// 移除 "idea" 后，得到字符串 "id"。

// 示例 2：

// 输入： s = "day"

// 输出： "day"

// 解释：

// 字符串 "day" 尾部没有元音字母。

// 示例 3：

// 输入： s = "aeiou"

// 输出： ""

// 解释：

// 移除 "aeiou" 后，得到字符串 ""。

 

// 提示：

// 1 <= s.length <= 100
// s 仅由小写英文字母组成。

#include "lc_pub.h"

class Solution {
public:
    string trimTrailingVowels(string s) {
        int n=s.size();
        int i=n-1;
        for (;i>=0;i--) {
            if (s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u') continue;
            break;
        }
        return s.substr(0, i+1);
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,-2,3,-4};

    Solution so;
    return 0;
}
