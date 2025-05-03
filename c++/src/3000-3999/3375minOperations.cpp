#include "lc_pub.h"


class Solution {
    public:
    int minOperations(vector<int>& nums, int k) {
        unordered_set<int> s;
        for (auto x: nums) {
            if (x < k) return -1;
            s.emplace(x);
        }
        if (s.find(k) == s.end()) return s.size();
        return s.size()-1;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{5,2,5,4,5};

    Solution so;
    cout << so.minOperations(nums, 2) << endl;
    return 0;
}
