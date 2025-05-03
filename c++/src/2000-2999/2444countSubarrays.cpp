#include "lc_pub.h"

class Solution {
    public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long ans = 0;
        auto calc = [&](int i, int j) -> long long {
            // 计算子区间 [i, j] 中的个数
            long long res = 0;
            int cnt1=0,cnt2=0;  // 达到最小值和最大值的个数
            int r = i-1;
            for (int l=i;l<=j;l++) {
                while (r+1 <=j && (cnt1==0 || cnt2==0)) {
                    r++;
                    if (nums[r]==minK)cnt1++;
                    if (nums[r]==maxK)cnt2++;
                }
                if (cnt1==0 || cnt2==0) break;
                res += j + 1 - r;
                if (nums[l]==minK)cnt1--;
                if (nums[l]==maxK)cnt2--;
            }

            return res;
        };
        vector<int> border;
        border.emplace_back(-1);
        int n = nums.size();
        for (int i=0;i<n;i++) {
            if (nums[i]>maxK || nums[i]<minK)
                border.emplace_back(i);
        }
        border.emplace_back(n);
        for (int i=0;i<border.size()-1;i++) {
            if (border[i]==border[i+1]) continue;
            ans += calc(border[i]+1, border[i + 1]-1);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,3,5,2,7,5};

    Solution so;
    cout << so.countSubarrays(arr,1,5) << endl;
    return 0;
}
