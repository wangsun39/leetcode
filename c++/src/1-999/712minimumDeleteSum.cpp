#include "lc_pub.h"

using namespace std;

class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int n1=s1.size(),n2=s2.size();
        vector<vector<int>> dp(n1, vector<int>(n2, INT_MAX));
        bool match=false;
        if (s1[0]==s2[0]) {
            dp[0][0]=0;
            match=true;
        }
        else dp[0][0]=s1[0]+s2[0];
        for (int i=1;i<n1;i++) {
            if (!match) {
                if (s1[i]==s2[0]) {
                    dp[i][0]=dp[i-1][0]-s2[0];
                    match=true;
                }
                else {
                    dp[i][0]=dp[i-1][0]+s1[i];
                }
            }
            else {
                dp[i][0]=dp[i-1][0]+s1[i];
            }
        }
        match=dp[0][0]==0;
        for (int j=1;j<n2;j++) {
            if (!match) {
                if (s1[0]==s2[j]) {
                    dp[0][j]=dp[0][j-1]-s1[0];
                    match=true;
                }
                else {
                    dp[0][j]=dp[0][j-1]+s2[j];
                }
            }
            else {
                dp[0][j]=dp[0][j-1]+s2[j];
            }
        }
        for (int i=1;i<n1;i++) {
            for (int j=1;j<n2;j++) {
                if (s1[i]==s2[j]) {
                    dp[i][j]=min(dp[i][j],dp[i-1][j-1]);
                }
                else {
                    dp[i][j]=min(dp[i-1][j]+s1[i],dp[i][j-1]+s2[j]);
                }
            }
        }
        return dp[n1-1][n2-1];
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays{8,1,6,6};
    Solution so;
    cout << so.minimumDeleteSum("sea", "eat") <<endl;
    return 0;
}