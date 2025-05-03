#include "lc_pub.h"

class Solution {
public:
int subsetXORSum(vector<int>& nums) {
    int n=nums.size();
    int _or = reduce(nums.begin(), nums.end(), 0, [](int a, int b) {
        return a|b;
    });
    // int ans = 0;
    // for (int i=0;i<32;i++) {
    //     if (_or & (1<<i)) {
    //         ans += (1 << i);
    //     }
    // }
    return _or << (n-1);
}

};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,3};
    // vector<vector<int>> grid = parseGrid("[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]");
    // cout << grid.size() << "  " << grid[0].size()<< endl;

    Solution so;
    auto v = so.subsetXORSum(nums);
    cout << v << endl;
    return 0;
}
