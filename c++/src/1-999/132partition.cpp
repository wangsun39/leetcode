#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
    
    vector<int> calc;  // 记忆化dfs的结果  
    public:
    int minCut(string s) {
        int n = s.size();
        vector<vector<int>> pal(n, vector<int>(n, -1));  // pal[i][j] 记忆化区间[i,j]是否是回文
        pal.resize(n);
        calc.resize(n+1,-1);
        for (auto& row : pal) {
            row.resize(n, -1); // 设置列数并填充 -1
        }
        auto check = [&](this auto && check, string &s, int l, int r) -> bool {  // [l, r]
            if (pal[l][r] > -1) return pal[l][r] == 1;
            if (l + 1 >= r) {
                pal[l][r] = (s[l] == s[r]);
                return pal[l][r] == 1;
            }
            if (s[l] != s[r]) {
                pal[l][r] = 0;
                return false;
            }
            return pal[l][r] = check(s, l + 1, r - 1);
        };
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++) {
                check(s,i,j);
            }
        auto dfs = [&](auto&& dfs, int start) -> int {  // this auto&& 是g++ 在C++23中支持的，允许lambda中递归
            if (calc[start] > -1) return calc[start];
            if (start==s.size()) {
                return calc[start] = 0;
            }
            int res = INT_MAX;
            for (int end=start;end<s.size();end++) {
                if (check(s,start,end)) {
                    res = min(res, dfs(dfs, end+1));
                }
            }
            return calc[start] = res + 1;
        };
        return dfs(dfs, 0) - 1;
    };
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    auto v = so.minCut("ab");
    // auto v = so.minCut("ababababababababababababcbabababababababababababa");
    cout << v << endl;
    return 0;
}
