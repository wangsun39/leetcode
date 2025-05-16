#include "lc_pub.h"

class Solution {
    public:
    vector<string> getWordsInLongestSubsequence(vector<string>& words, vector<int>& groups) {
        int n = words.size();

        auto dist = [&](string &w1, string &w2) -> int {
            int res=0;
            for (int i=0;i<w1.size();i++)
                if (w1[i]!=w2[i]) res++;

            return res;
        };
        vector<int> dp(n, 1);
        vector<int> pre(n, -1);
        int mx = 1;
        int mxi = 0;
        for (int i=1;i<n;i++) {
            for (int j=i-1;j>=0;j--) {
                if (groups[i]==groups[j] || words[i].size() != words[j].size()) continue;
                if (1 == dist(words[i], words[j])) {
                    if (dp[j] + 1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                        pre[i] = j;
                        if (mx < dp[i]) {
                            mx = dp[i];
                            mxi = i;
                        }
                    }
                }
            }
        }
        vector<string> ans(mx);
        for (int i = mx - 1;i>=0;i--) {
            ans[i] = words[mxi];
            mxi = pre[mxi];
        }

        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    // vector<string> nums1{"cb","dc","ab","aa","ac","bb","ca","bcc","cdd","aad","bba","bc","ddb"};
    // vector<int> nums2{12,6,10,11,4,8,9,11,2,11,3,2,5};
    vector<string> nums1{"cb","dcc","da","cbb","bd","dbc","ab","db"};
    vector<int> nums2{4,5,5,7,8,1,3,4};

    Solution so;
    cout << so.getWordsInLongestSubsequence(nums1, nums2) << endl;
    return 0;
}
