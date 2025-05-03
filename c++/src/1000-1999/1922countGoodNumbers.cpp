#include "lc_pub.h"

class Solution {
public:
int countGoodNumbers(long long n) {
    long long odds = n / 2;
    long long even = n - odds;
    long long MOD = 1000000007;
    vector<long long> p5, p4;
    p5.emplace_back(5);
    p4.emplace_back(4);
    int ans=1;
    for (int i=0;i<65;i++) {
        p5.emplace_back(p5.back() * p5.back() % MOD);
        p4.emplace_back(p4.back() * p4.back() % MOD);
    }
    cout<<p4<<endl;
    cout<<p5<<endl;
    auto pow = [&] (vector<long long> base, long long m) -> long long {
        long long res = 1;
        for (int i=0;i<65;i++) {
            if (m==0) break;
            if (m & 1) {
                res *= base[i];
                res %= MOD;
            }
            m >>= 1;
        }
        return res;
    };

    return (pow(p5, even) * pow(p4, odds)) % MOD;

}

};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,3};
    // vector<vector<int>> grid = parseGrid("[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]");
    // cout << grid.size() << "  " << grid[0].size()<< endl;

    Solution so;
    auto v = so.countGoodNumbers(50);
    cout << v << endl;
    return 0;
}
