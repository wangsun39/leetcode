#include "lc_pub.h"

class Solution {
    public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        int MOD=1'000'000'007;
        vector<int>pow2;
        for (int i=0;i<32;i++) {
            if (n & (1 << i))
                pow2.emplace_back(1 << i);
        }
        int m = pow2.size();
        vector res(m, vector<int>(m));
        for (int i=0;i<m;i++) {
            res[i][i] = pow2[i];
            for (int j=i+1;j<m;j++) {
                res[i][j] = ((long long)res[i][j-1] * pow2[j]) % MOD;
            }
        }
        vector<int> ans;
        for (int i=0;i<queries.size();i++) {
            ans.emplace_back(res[queries[i][0]][queries[i][1]]);
        }
        return ans;
    }

    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {4,1,3,3};

    Solution so;
    cout << so.productQueries("bdda") << endl;
    return 0;
}
