#include "lc_pub.h"

int dp[1001][26];

class Solution {
public:
    int longestBalanced(string s) {
        int n = s.size();
        memset(dp,0,size(dp[0])*n);
        if (n == 0) return 1;
        vector<int> si(n);
        for (int i = 0; i < n; ++i) {
            si[i] = s[i] - 'a';
        }

        int ans = 1;
        dp[1][si[0]] = 1;

        for (int i = 1; i <= n; ++i) {
            memcpy(dp[i], dp[i-1], sizeof(dp[0]));
            dp[i][si[i - 1]] += 1;
            for (int j = 0; j < i; ++j) {
                if (i - j + 1 <= ans) break;
                int ch = -1;
                bool flg=true;
                for (int k = 0; k < 26; ++k) {
                    int val = dp[i][k] - dp[j][k];
                    if (val==0) continue;
                    if (ch==-1) {
                        ch = val;
                    }
                    else if (ch!=val) {
                        flg=false;
                        break;
                    }
                }
                if (!flg) continue;
                ans = i - j;
                break;
            }
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,5,6,7};

    Solution so;
    return 0;
}
