#include "lc_pub.h"

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> up;
            int i = 0;
            for (int x : nums){
                if (up.find(target - x) != up.end())
                    return vector<int>{up[target - x], i};
                up[x] = i;
                i++;
            }
            return {};
        }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> nums = {4, 5, 6};
    Solution so;
    auto v = so.twoSum(nums, 9);
    cout << v << endl;
    return 0;
}
