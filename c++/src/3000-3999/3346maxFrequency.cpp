#include "lc_pub.h"

class Solution {
    
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        vector<int>unique;
        unordered_map<int,int>counter;
        int n=nums.size();
        for (int i=0;i<n;i++) {
            counter[nums[i]]++;
            if (counter[nums[i]]==1) unique.push_back(nums[i]);
        }
        int ans=0;
        ranges::sort(nums);
        for (int x=nums[0];x<=nums[n-1];x++) {
            auto p1 = ranges::lower_bound(nums, x-k);
            auto p2 = ranges::upper_bound(nums, x+k);
            cout<<p2-p1<<endl;
            ans=max(ans,min((int)(p2-p1)-counter[x],numOperations) + counter[x]);
        }
        return ans;
    }
};


    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {5};

    Solution so;
    // so.addText("leetcode");
    cout << so.maxFrequency(arr,0,0) << endl;
    return 0;
}
