#include "lc_pub.h"

class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        const int MOD = 1e9 + 7;
        long long counter[2][26] = {0};
        for (auto x:s) 
            counter[0][x-'a']++;
        int src,dst;

        for (int i=0;i<t;i++) {
            if ((i & 1) == 0) {
                src=0,dst=1;
            }
            else {
                src=1,dst=0;
            }
            for (int j=1;j<26;j++) {
                counter[dst][j] = counter[src][j - 1];
            }
            counter[dst][0] = counter[src][25];
            counter[dst][1] += counter[src][25] % MOD;
        }
        long long ans=0;
        for (int i=0;i<26;i++) {
            ans += counter[dst][i];
            ans %= MOD;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    cout << so.lengthAfterTransformations("abcyy", 2) << endl;
    return 0;
}
