#include "lc_pub.h"


class Solution {
    public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        endTime.insert(endTime.begin(),0);
        startTime.emplace_back(eventTime);
        int s=0;
        for (int i=0;i<k;i++) s+=endTime[i+1]-startTime[i];
        int ans=0;
        for (int i=0;i<n+1;i++) {
            ans = max(ans, startTime[i+k]-endTime[i]-s);
            if (i+k+1>=n+1) break;
            s += endTime[i+k+1]-startTime[i+k] - (endTime[i+1]-startTime[i]);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums1{1,3}, nums2{2,5};

    Solution so;
    cout << so.maxFreeTime(5,1,nums1,nums2) << endl;
    return 0;
}
