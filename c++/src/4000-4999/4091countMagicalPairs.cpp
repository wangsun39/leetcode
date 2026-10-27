// 给你一个长度为 n 且仅由小写英文字母组成的字符串 s。

// 对于满足 0 <= i <= j < k < n 的每一个下标三元组 (i, j, k)，定义：

// s1 = s[i..j]
// s2 = s[j + 1..k]
// 如果 s1 中不同字符的数量等于 s2 中不同字符的数量，则称这对子字符串 (s1, s2) 是神奇的。

// 返回满足 (s1, s2) 是神奇对的三元组 (i, j, k) 的数量。

// 子字符串是字符串中连续的非空字符序列。

 

// 示例 1：

// 输入： s = "aba"

// 输出： 2

// 解释：

// 有 2 个有效的三元组：

// 编号	(i, j, k)	s1	s2	distinct(s1)	distinct(s2)
// 1	(0, 0, 1)	"a"	"b"	1	1
// 2	(1, 1, 2)	"b"	"a"	1	1
// 示例 2：

// 输入： s = "kkk"

// 输出： 4

// 解释：

// 有 4 个有效的三元组：

// 编号	(i, j, k)	s1	s2	distinct(s1)	distinct(s2)
// 1	(0, 0, 1)	"k"	"k"	1	1
// 2	(0, 0, 2)	"k"	"kk"	1	1
// 3	(0, 1, 2)	"kk"	"k"	1	1
// 4	(1, 1, 2)	"k"	"k"	1	1
// 示例 3：

// 输入： s = "abcac"

// 输出： 7

// 解释：

// 有 7 个有效的三元组：

// 编号	(i, j, k)	s1	s2	distinct(s1)	distinct(s2)
// 1	(0, 0, 1)	"a"	"b"	1	1
// 2	(1, 1, 2)	"b"	"c"	1	1
// 3	(2, 2, 3)	"c"	"a"	1	1
// 4	(3, 3, 4)	"a"	"c"	1	1
// 5	(0, 1, 3)	"ab"	"ca"	2	2
// 6	(0, 1, 4)	"ab"	"cac"	2	2
// 7	(1, 2, 4)	"bc"	"ac"	2	2
 

// 提示：

// 2 <= s.length <= 105
// s 仅由小写英文字母组成。


#include "lc_pub.h"

class Solution {
public:
    long long countMagicalPairs(string s) {
        int n=s.size();
        unordered_set<char> st;
        for (char c : s) {
            st.insert(c);
        }
        long long ans=0;
        int m=st.size();  // 不同字母个数
        for (int i=1;i<=m;i++) {
            vector<int>left(n, 0),right(n, 0);  // 以s[j]结尾，不同字母个数为 i 的个数为left[j]，s[j]开头，不同字母个数为 i 的个数为right[j]

            int c1[26]={0},c2[26]={0},cc1=0,cc2=0;
            int l1=0,l2=0,r=0;  // 左端点在 [l1, l2] 之间，右端点在r处，的子数组不同字母个数都是 i
            // c1 对应 [l1, r] 之间的计数， c2 对应 [l2, r] 之间的计数
            for (r=0;r<n;r++) {
                if(++c1[s[r]-'a'] == 1){cc1++;}
                if(++c2[s[r]-'a'] == 1){cc2++;}
                if (cc1<i) continue;
                while (cc1>i) {
                    if(--c1[s[l1]-'a'] == 0){cc1--;}
                    l1++;
                }
                while (cc2>=i) {
                    if(--c2[s[l2]-'a'] == 0){cc2--;}
                    l2++;
                }
                left[r]=l2-l1;
            }

            // 对称处理 right
            memset(c1,0,sizeof(c1));
            memset(c2,0,sizeof(c2));
            int r1=n-1,r2=n-1,l=0;
            cc1=0,cc2=0;
            for (l=n-1;l>=0;l--) {
                if(++c1[s[l]-'a'] == 1){cc1++;}
                if(++c2[s[l]-'a'] == 1){cc2++;}
                if (cc1<i) continue;
                while (cc1>i) {
                    if(--c1[s[r1]-'a'] == 0){cc1--;}
                    r1--;
                }
                while (cc2>=i) {
                    if(--c2[s[r2]-'a'] == 0){cc2--;}
                    r2--;
                }
                right[l]=r1-r2;
            }
            for (int j=0;j<n-1;j++) {
                ans+=(long long)left[j]*right[j+1];
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{-58,4,24,23};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");
    Solution so;
    cout<<so.countMagicalPairs("abcaac")<<endl;

    return 0;
}
