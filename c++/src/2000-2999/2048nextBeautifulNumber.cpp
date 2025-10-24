#include "lc_pub.h"

class Solution {
    vector<int> nums;
public:
    Solution() {
        nums.push_back(666666);
        nums.push_back(1224444);
        vector<vector<int>> a = {{1},{2,2},{3,3,3},{1,2,2},{1,3,3,3},{4,4,4,4},{1,4,4,4,4},{2,2,3,3,3},{5,5,5,5,5},{1,2,2,3,3,3},{1,5,5,5,5,5},{2,2,4,4,4,4}};
        for (auto &b: a) {
            do {
                int v=0;
                for (int c: b) v=v*10+c;
                nums.push_back(v);
            } while (std::next_permutation(b.begin(), b.end()));
        }
        ranges::sort(nums);
    }
    int nextBeautifulNumber(int n) {
        auto x=ranges::upper_bound(nums, n);
        return *x;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {3,1};

    Solution so;
    cout << so.nextBeautifulNumber(1) << endl;
    return 0;
}
