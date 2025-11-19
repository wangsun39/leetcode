#include "lc_pub.h"

class Solution {
    public:
    int findFinalValue(vector<int>& nums, int original) {
        unordered_set<int> s;
        for (int x: nums) s.insert(x);
        while (s.find(original) != s.end()) {
            original *= 2;
        }
        return original;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr{1,-3,4};

    Solution so;
    return 0;
}
