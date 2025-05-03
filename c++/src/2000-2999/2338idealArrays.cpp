#include "lc_pub.h"

const int MOD = 1'000'000'007;
const int MAX_N = 10'000;
const int MAX_E = 13;

vector<int> EXP[MAX_N + 1]; 
int C[MAX_N + MAX_E][MAX_E + 1];

int init1 = []() {
    // EXP[x] 为 x 分解质因数后，每个质因数的指数
    for (int x = 2; x <= MAX_N; x++) {
        int t = x;
        for (int i = 2; i * i <= t; i++) {
            int e = 0;
            for (; t % i == 0; t /= i) {
                e++;
            }
            if (e) {
                EXP[x].push_back(e);
            }
        }
        if (t > 1) {
            EXP[x].push_back(1);
        }
    }
    return 0;
}();

int init2 = []() {
    // 预处理组合数
    for (int i = 0; i < MAX_N + MAX_E; i++) {
        C[i][0] = 1;
        for (int j = 1; j <= min(i, MAX_E); j++) {
            C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % MOD;
        }
    }
    return 0;
}();

class Solution {
    public:
        int idealArrays(int n, int maxValue) {
            long long ans = 1;
            for (int i=2;i<=maxValue;i++) {
                long long res = 1;
                for (int x: EXP[i]) {
                    // x 是 i 的某个质因子的个数，质因数是多少并不重要
                    res *= C[n + x - 1][x];
                    res %= MOD;
                }
                ans += res;
                ans %= MOD;
            }
            return ans;
        }
    };
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    Solution so;
    cout << so.idealArrays(2,5) << endl;
    return 0;
}
