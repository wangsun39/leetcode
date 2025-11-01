#include "lc_pub.h"


class Solution {
    public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        unordered_set<int> vis;
        vector<int> ans;
        for (int x: nums) {
            if (vis.end() == vis.find(x)) {
                vis.insert(x);
            }
            else
                ans.push_back(x);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{5,2,5,4,5};

    Solution so;
    return 0;
}
