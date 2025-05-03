#include "lc_pub.h"

class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        int n = position.size();
        sort(position.begin(), position.end());

        auto dfs = [&](int val) -> bool {
            int start = position[0];
            int acc = 1;
            for (int i = 0; i < n; i++) {
                int x = position[i];
                if (x - start >= val) {
                    start = x;
                    acc++;
                    if (acc == m) return true;
                }
            }
            return false;
        };
        // int lo = 0, hi = *max_element(position.begin(), position.end());
        int lo = 0, hi = position.back();
        while (lo + 1 < hi) {
            int mid = (lo + hi) / 2;
            if (dfs(mid)) 
                lo = mid;
            else
                hi = mid;
        }
        return lo;

    }

};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> p = {1,2,3,4,7};
    Solution so;
    auto v = so.maxDistance(p, 3);
    cout << v << endl;
    return 0;
}
