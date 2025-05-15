#include "lc_pub.h"

class Solution {
    static constexpr int MOD = 1'000'000'007;
    static constexpr int SIZE = 26;

    using Matrix = array<array<int, SIZE>, SIZE>;

    // 返回矩阵 a 和矩阵 b 相乘的结果
    Matrix mul(Matrix& a, Matrix& b) {
        Matrix c{};
        for (int i = 0; i < SIZE; i++) {
            for (int k = 0; k < SIZE; k++) {
                if (a[i][k] == 0) {
                    continue;
                }
                for (int j = 0; j < SIZE; j++) {
                    c[i][j] = (c[i][j] + (long long) a[i][k] * b[k][j]) % MOD;
                }
            }
        }
        return c;
    }

    // 返回 n 个矩阵 a 相乘的结果
    Matrix pow(Matrix a, int n) {
        Matrix res = {};
        for (int i = 0; i < SIZE; i++) {
            res[i][i] = 1; // 单位矩阵
        }
        while (n) {
            if (n & 1) {
                res = mul(res, a);
            }
            a = mul(a, a);
            n >>= 1;
        }
        return res;
    }


public:
    int lengthAfterTransformations(string s, int t, vector<int>& nums) {
        Matrix mat{};
        for (int i=0;i<SIZE;i++) {
            for (int j=0;j<nums[i];j++) {
                mat[i][(i+1+j)%SIZE]=1;
            }
        }
        int v[SIZE]={0};
        for (auto x: s) v[x-'a']++;
        Matrix mat2=pow(mat, t);

        long long ans=0;
        for (int i=0;i<SIZE;i++) {
            ans += reduce(mat2[i].begin(), mat2[i].end(), 0LL) * v[i];
            ans %= MOD;
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2};

    Solution so;
    cout << so.lengthAfterTransformations("abcyy", 2, nums) << endl;
    return 0;
}
