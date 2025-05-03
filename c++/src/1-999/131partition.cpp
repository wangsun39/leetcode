#include "lc_pub.h"

class Solution1 {
    bool isPalindrome(string& s, int left, int right) {
        while (left < right) {
            if (s[left++] != s[right--]) {
                return false;
            }
        }
        return true;
    }

public:
    vector<vector<string>> partition(string s) {
        int n = s.length();
        vector<vector<string>> ans;
        vector<string> path;

        // start 表示当前这段回文子串的开始位置
        auto dfs = [&](auto&& dfs, int i, int start) {
            if (i == n) {
                ans.emplace_back(path);
                return;
            }

            // 不选 i 和 i+1 之间的逗号（i=n-1 时一定要选）
            if (i < n - 1) {
                dfs(dfs, i + 1, start);
            }

            // 选 i 和 i+1 之间的逗号（把 s[i] 作为子串的最后一个字符）
            if (isPalindrome(s, start, i)) {
                path.push_back(s.substr(start, i - start + 1));
                dfs(dfs, i + 1, i + 1); // 下一个子串从 i+1 开始
                path.pop_back(); // 恢复现场
            }
        };

        dfs(dfs, 0, 0);
        return ans;
    }
};


class Solution {
    bool check(string &s, int l, int r) {
        for (int i=0;i<(r-l)/2;i++) {
            if (s[l+i] != s[r-1-i]) return false;
        }
        return true;
    }
    public:
    vector<vector<string>> partition(string s) {
        auto dfs = [&](auto&& dfs, int start) -> vector<vector<string>> {  // this auto&& 是g++ 在C++23中支持的，允许lambda中递归
            if (start==s.size()) return {{}};
            vector<vector<string>> res;
            for (int end=start+1;end<=s.size();end++) {
                if (check(s,start,end)) {
                    auto arr=dfs(dfs, end);
                    for (auto &arr2: arr) {
                        arr2.emplace_back(s.substr(start, end - start));
                        res.emplace_back(arr2);
                    }
                }
            }
            return res;
        };
        auto ans = dfs(dfs, 0);
        for (auto &arr: ans) {
            reverse(arr.begin(), arr.end());
        }
        return ans;
    };
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    auto v = so.partition("abbab");
    // cout << v << endl;
    return 0;
}
