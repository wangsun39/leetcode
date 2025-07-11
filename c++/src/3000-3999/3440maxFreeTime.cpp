#include "lc_pub.h"


class Solution {
    public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        endTime.insert(endTime.begin(),0);
        startTime.emplace_back(eventTime);
        if (n==1) return eventTime-(endTime[1]-startTime[0]);
        vector<int> interval;  // 至少有3个间隔
        for (int i=0;i<=n;i++)
            interval.push_back(startTime[i]-endTime[i]);
        ranges::sort(interval, greater<int>());
        int ans=0;
        for (int i=0;i<n;i++) {
            ans = max(ans, startTime[i]-endTime[i]+startTime[i+1]-endTime[i+1]);
            int m=endTime[i+1]-startTime[i]; // 当前的会议时间
            int iv1 = startTime[i]-endTime[i];
            int iv2 = startTime[i+1]-endTime[i+1];
            vector<int>top3(interval.begin(), interval.begin()+3);
            auto it = find(top3.begin(), top3.end(), iv1);
            if (it!=top3.end()) top3.erase(it);
            it = find(top3.begin(), top3.end(), iv2);
            if (it!=top3.end()) top3.erase(it);
            if (m<=top3[0]) 
                ans = max(ans, startTime[i+1]-endTime[i]);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums1{1,3}, nums2{2,5};

    Solution so;
    cout << so.maxFreeTime(5,nums1,nums2) << endl;
    return 0;
}
