#include "lc_pub.h"

class RangeFreqQuery {
public:
int maximumCandies(vector<int>& candies, long long k) {
    auto check = [&](long long val)->bool {
        long long cnt = 0;
        for (auto x: candies) {
            cnt += x / val;
        }
        return cnt >= k;
    };
    if (reduce(candies.begin(), candies.end(), 0LL)<k) return 0;
    long long lo=1, hi=(long long)ranges::max(candies) + 1;
    while (lo < hi - 1) {
        long long mid = (lo +hi)/2;
        if (check(mid)) lo=mid;
        else hi=mid;
    }
    return lo;
}
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {5,8,6};

    RangeFreqQuery so;
    cout << so.maximumCandies(arr, 3) << endl;
    return 0;
}
