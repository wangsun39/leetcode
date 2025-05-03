#pragma once

#include "lc_pub.h"
 
const int MX = 101;
bool primes[MX];


auto init = [] {
    memset(primes, true, MX);
    primes[1] = false;
    for (int i = 2; i * i < MX; i++) {
        if (!primes[i]) continue;
        for (int j = i * i; j < MX; j += i) {
            primes[j] = false; // j 是质数 i 的倍数
        }
    }
    return 0;
}();

const int MOD = 1'000'000'007;
const int MAX_N = 10'000;
const int MAX_E = 13;

vector<int> EXP[MAX_N + 1]; 
int C[MAX_N + MAX_E][MAX_E + 1];  // 组合数 comb(n, m)

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



// 乘法快速幂
class Solution {
    const int MOD = 1'000'000'007;

    long long qpow(long long x, long long n) {
        long long res = 1;
        while (n) {
            if (n & 1) {
                res = res * x % MOD;
            }
            x = x * x % MOD;
            n >>= 1;
        }
        return res;
    }
};

