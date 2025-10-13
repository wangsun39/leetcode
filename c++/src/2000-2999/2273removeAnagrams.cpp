#include "lc_pub.h"

class Solution {
    public:
    vector<string> removeAnagrams(vector<string>& words) {
        vector<string> ans;
        ans.push_back(words[0]);
        string cur = words[0];
        ranges::sort(cur);
        int n = words.size();
        for (int i=1;i<n;i++) {
            string s = words[i];
            ranges::sort(s);
            if (cur==s) continue;
            ans.push_back(words[i]);
            cur = s;
        }
        return ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    return 0;
}
