// 给你两个长度相同的字符串 s1 和 s2。

// 不匹配片段 是一个 极大连续 下标区间，其中每个下标处 s1 和 s2 的字符都不相同。

// 返回一个二维数组，其中包含每个不匹配片段对应的 [sub1, sub2]，sub1 和 sub2 分别是 s1 和 s2 中对应的 子字符串。请按片段起始下标的 递增 顺序返回。如果没有不匹配片段，则返回一个空数组。

 

// 示例 1：

// 输入： s1 = "earth", s2 = "empty"

// 输出： [["ar","mp"],["h","y"]]

// 解释：

// 下标 1 和 2 处的字符不同，形成不匹配片段 ["ar","mp"]。
// 下标 4 处的字符不同，形成不匹配片段 ["h","y"]。
// 示例 2：

// 输入： s1 = "action", s2 = "nation"

// 输出： [["ac","na"]]

// 解释：

// 下标 0 和 1 处的字符不同，形成不匹配片段 ["ac","na"]。两个字符串中其余位置的字符均相同。

// 示例 3：

// 输入： s1 = "hot", s2 = "hot"

// 输出： []

// 解释：

// 两个字符串完全相同，因此没有不匹配片段。

 

// 提示：

// 1 <= s1.length == s2.length <= 100
// s1 和 s2 仅由小写英文字母组成。


#include "lc_pub.h"

class Solution {
public:
    vector<vector<string>> findMismatchedSegments(string s1, string s2) {
        int n=s1.size(),l=-1;
        vector<vector<string>> ans;
        vector<int>ids(1, -1);
        for (int i=0;i<n;i++) {
            if (s1[i]==s2[i]) {
                ids.push_back(i);
            }
        }
        ids.push_back(n);

        for (int i=0;i<ids.size()-1;i++) {
            if(ids[i+1]-ids[i]==1) continue;
            ans.push_back({s1.substr(ids[i]+1,ids[i+1]-ids[i]-1), s2.substr(ids[i]+1,ids[i+1]-ids[i]-1)});
        }

        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    string s1 = "earth";
    string s2 = "empty";
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");
    Solution so;
    cout<<so.findMismatchedSegments(s1,s2)<<endl;

    return 0;
}
