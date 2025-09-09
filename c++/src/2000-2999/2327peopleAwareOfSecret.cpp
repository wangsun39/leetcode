#include "lc_pub.h"


class Solution {
    public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        int MOD=1'000'000'007;
        vector<long long> diff(n, 0);   // 知道秘密的人数的差分数组，实际只存储需要减少的部分
        vector<long long> diff2(n, 0);  // 可以传递秘密的人数的差分数组
        long long num1=1, num2=0;
        diff2[delay] = 1;
        if (forget < n) {
            diff[forget] -= 1;
            diff2[forget] -= 1;
        }
        for (int i=0;i<n;i++) {
            num2=(num2+diff2[i]+MOD)%MOD;  // 当天可以传递秘密的人数
            num1=(num1+diff[i]+num2+MOD)%MOD;  // 当天知道秘密的人数增加了 diff[i]+num2，其中nums2是增加的部分，diff[i]是通过差分需要减的部分
            if (i+delay<n) {
                diff2[i+delay]+=num2;
            }
            if (i+forget<n) {
                diff[i+forget]-=num2;
                diff2[i+forget]-=num2;
            }
            // cout<<num1<<","<<num2<<endl;
        }
        return num1;
    }
    };
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    cout << so.peopleAwareOfSecret(6, 2, 4) << endl;
    return 0;
}
