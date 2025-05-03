#include "lc_pub.h"

class Solution {
    public:
    int countPairs(vector<int>& nums, int k) {
        int n = nums.size();
        int ans=0;
        for (int i=0;i<n;i++) {
            for (int j=i+1;j<n;j++) {
                if ((i * j) % k == 0 && nums[i]==nums[j]) ans++;
            }
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {3,1,2,2,2,1,3};

    Solution so;
    cout << so.countPairs(arr, 2) << endl;
    return 0;
}
