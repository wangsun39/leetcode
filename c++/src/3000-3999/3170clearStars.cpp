#include "lc_pub.h"


class Solution {
    public:
    string clearStars(string s) {
        int n = s.size();
        vector<int> flag(n,0);  // 是否删除
        // map<char, stack<int>> list;
        stack<int> list[26];
        for (int i=0;i<n;i++) {
            if (s[i]=='*') {
                for (int j=0;j<26;j++) {
                    if (!list[j].size()) continue;
                    int k = list[j].top();
                    flag[k] = 1;
                    list[j].pop();
                    break;
                }
                flag[i]=1;
            }
            else {
                list[s[i]-'a'].push(i);
            }
        }
        string ans="";
        for (int i=0;i<n;i++) {
            if (!flag[i]) ans+=s[i];
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,3,3};

    Solution so;
    cout << so.clearStars("aaba*") << endl;
    return 0;
}
