#include "lc_pub.h"


class Solution {
    public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int,int>counter;
        int ans=0,mx=0;
        for (int x: nums) {
            counter[x]++;
            if (counter[x] > mx) {
                mx=counter[x];
                ans=mx;
            }
            else if (counter[x] == mx) {
                ans+=mx;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,3,3};

    Solution so;
    return 0;
}
