#include "lc_pub.h"

class Solution {
    public:
    long long maxPower(vector<int>& stations, int r, int k) {
        long long lo=stations[0], hi=k+1;
        int n=stations.size();
        for (int i=0;i<n;i++) {
            lo = min(lo, (long long)stations[i]);
            hi += stations[i];
        }

        auto check = [&](long long val) -> bool {
            vector<long long> st(n,0LL);
            for (int i=0;i<n;i++) st[i]=stations[i];
            long long lk=k;
            long long s=0;
            for (int i=0;i<=r;i++) {
                s+=st[i];
            }
            if (s<val) {
                st[r]+=val-s;
                lk-=val-s;
                if (lk<0) return false;
                s=val;
            }
            for (int i=1;i<n;i++) {
                int ri=i+r;
                if (ri<n)
                    s+=st[ri];
                if (i-r-1>=0) {
                    s-=st[i-r-1];
                }
                ri=min(ri,n-1);
                if (s<val) {
                    st[ri]+=val-s;
                    lk-=val-s;
                    if (lk<0) return false;
                    s=val;
                }
            }
            return true;
        };

        while (lo + 1 < hi) {
            long long mid=(lo+hi)/2;
            if (check(mid))
                lo = mid;
            else
                hi = mid;
        }
        return lo;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {13,12,8,14,7};

    Solution so;
    cout << so.maxPower(arr, 2,23) << endl;
    return 0;
}
