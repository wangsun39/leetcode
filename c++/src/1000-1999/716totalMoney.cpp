#include "lc_pub.h"

class Solution {
public:
    int totalMoney(int n) {
        int weeks = n / 7, days = n % 7;
        int ans = weeks * 28 + weeks * (weeks - 1) / 2 * 7;
        ans += (weeks + 1) * days + days * (days - 1) / 2;
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> grid = parseGrid("[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]");
    cout << grid.size() << "  " << grid[0].size()<< endl;

    Solution so;
    return 0;
}
