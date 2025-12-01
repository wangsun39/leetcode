#include "lc_pub.h"

class Solution {
    public:
    long long maxRunTime(int n, vector<int>& batteries) {
        long long s = 0;
        for (int x: batteries) s += x;
        
        auto check=[&](long long v) -> bool {
            long long ss = 0;
            for (int x: batteries) {
                if (x >= v) ss += v;
                else ss+=x;
            }
            return ss>=v*n;
        };
        long long lo=1,hi=s/n+1;
        while (lo<hi-1) {
            long long mid=(lo+hi)/2;
            if (check(mid))
                lo=mid;
            else
                hi=mid;
        }
        return lo;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    // auto arr = parseGrid("[[3,2],[4,3],[4,4],[2,5]]");

    Solution so;
    return 0;
}
