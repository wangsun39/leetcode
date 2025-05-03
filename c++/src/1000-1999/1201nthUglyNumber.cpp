#include "lc_pub.h"

using namespace std;

class Solution {
public:
int nthUglyNumber(int n, int a, int b, int c) {
    auto check = [&](long long val)->bool {
        long long gab = lcm((long long)a, (long long)b);  // 要转成 long long
        long long gbc = lcm((long long)b, (long long)c);
        long long gac = lcm((long long)a, (long long)c);
        long long gabc = lcm(gab , (long long)c);
        cout<<val / a + val / b + val / c - val / gab - val / gbc - val / gac + val / gabc<<' ' << n<<endl;
        return val / a + val / b + val / c - val / gab - val / gbc - val / gac + val / gabc >= n;
    };
    long long lo=0, hi = 2 * 1000000000;
    while (lo < hi - 1) {
        long long mid = (lo + hi) / 2;
        if (check(mid))
            hi = mid;
        else
            lo = mid;
        cout<<mid<<endl;
    }
    return hi;
}
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> arrays = parseGrid("[[1,2,3],[4,5],[1,2,3]]");
    Solution so;
    cout << so.nthUglyNumber(1000000000,2,217983653,336916467) <<endl;
    return 0;
}