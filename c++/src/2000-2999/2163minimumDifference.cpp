#include "lc_pub.h"

class Solution {
    public:
    long long minimumDifference(vector<int>& nums) {
        long long ans=INT64_MAX;
        int n = nums.size()/3;
        priority_queue<int> pq1;
        priority_queue<int, vector<int>, greater<int>> pq2;
        vector<long long> left(n * 3, 0), right(n * 3, 0);  // 位置i及i左侧n项最小值和右侧n项最大值
        long long s=0;
        for (int i=0;i<=n*2;i++) {
            if (i<n) {
                pq1.emplace(nums[i]);
                s+=nums[i];
            }
            else if (pq1.top()>nums[i]) {
                s += nums[i] - pq1.top();
                pq1.pop();
                pq1.emplace(nums[i]);
            }
            left[i]=s;
        }
        s=0;
        for (int i=n*3-1;i>=n;i--) {
            if (i>=n*2) {
                pq2.emplace(nums[i]);
                s+=nums[i];
            }
            else if (pq2.top()<nums[i]) {
                s += nums[i] - pq2.top();
                pq2.pop();
                pq2.emplace(nums[i]);
            }
            right[i]=s;
        }
        for (int i=n-1;i<n*2;i++) {
            ans = min(ans,left[i]-right[i+1]);
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {3,1,2};

    Solution so;
    cout << so.minimumDifference(arr) << endl;
    return 0;
}
