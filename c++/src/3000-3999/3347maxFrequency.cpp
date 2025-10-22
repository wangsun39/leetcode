#include "lc_pub.h"

class Solution {
    
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        vector<int>unique;
        unordered_map<int,int>diff;
        unordered_map<int,int>counter;
        int n=nums.size();
        for (int i=0;i<n;i++) {
            diff[nums[i]-k]++;
            diff[nums[i]+k+1]--;
            diff[nums[i]];
            counter[nums[i]]++;
        }
        vector<pair<int,int>> d_pairs;
        for (auto&[k,v]: diff) {
            d_pairs.push_back({k, v});
        }
        int ans=0, cur=0;
        ranges::sort(d_pairs);
        for (auto&[k,v]: d_pairs) {
            cur+=v;
            ans=max(ans,min(numOperations,cur - counter[k])+counter[k]);
        }
        return ans;
    }
};


    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,4,5};

    Solution so;
    // so.addText("leetcode");
    cout << so.maxFrequency(arr,1,2) << endl;
    return 0;
}
