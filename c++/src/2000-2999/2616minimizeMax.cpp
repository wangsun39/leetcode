#include "lc_pub.h"

class Solution {
    public:
    int minimizeMax(vector<int>& nums, int p) {
        int n = nums.size();
        ranges::sort(nums);
        if (p==0) return 0;
        auto check = [&](int val)->bool {
            int i=0;
            int cnt = 0;
            while (i<n-1) {
                if (nums[i+1]-nums[i]>val) {
                    i++;
                    continue;
                }
                i+=2;
                cnt++;
                if (cnt>=p) return true;
            }
            return false;
        };
        int lo=-1,hi=nums[n-1]-nums[0];
        while (lo+1<hi) {
            int mid=(lo+hi)/2;
            if (check(mid))
                hi=mid;
            else
                lo=mid;
        }
        return hi;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {10,1,2,7,1,3};

    Solution so;
    cout << so.minimizeMax(arr, 2) << endl;
    return 0;
}
