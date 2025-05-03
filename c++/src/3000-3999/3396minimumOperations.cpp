#include "lc_pub.h"


class Solution {
    public:
    int minimumOperations(vector<int>& nums) {
        unordered_map<int, int>counter;
        unordered_set<int> large;
        for (auto x: nums) {
            counter[x]++;
            if (counter[x] > 1) large.emplace(x);
        }
        int n = nums.size();
        for (int i=0;i<n;i+=3) {
            if (large.size()==0) return i/3;
            for (int j=0;j<3 && i+j<n;j++) {
                counter[nums[i+j]]-=1;
                if (counter[nums[i+j]]==1) large.erase(nums[i+j]);
            }
            
        }
        return (n+2)/3;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3,4,2,3,3,5,7};

    Solution so;
    cout << so.minimumOperations(nums) << endl;
    return 0;
}
