#include "lc_pub.h"


class Solution {
    public:
    int longestSubsequence(string s, int k) {
        int ans=0,n=s.size();
        long long mx=0;
        for (int j=0;j<n;j++) {
            if (s[n-1-j]=='0') {
                ans++;
                continue;
            }
            if (j<=32 && (mx + (1 << j))<=k) {
                mx += (1 << j);
                ans++;
            }                
        }
        return ans;
    }
    };
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {9,5,3,8,4,7,2,7,4,5,4,9,1,4,8,10,8,10,4,7};

    Solution so;
    cout << so.longestSubsequence("1001010", 5) << endl;
    return 0;
}
