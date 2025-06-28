#include "lc_pub.h"

class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> idx(n, 0);
        ranges::iota(idx, 0);  // 从0开始的递增序列
        ranges::sort(idx, {}, [&](int i) {return -nums[i];});

        idx.resize(k);
        ranges::sort(idx);
        vector<int> ans(k, 0);
        for (int i=0;i<k;i++) {
            ans[i]=nums[idx[i]];
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {2,1,3,3};

    Solution so;
    cout << so.maxSubsequence(arr, 2) << endl;
    return 0;
}
