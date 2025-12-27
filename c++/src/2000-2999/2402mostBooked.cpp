#include "lc_pub.h"

class Solution {
    public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        ranges::sort(meetings, {}, [](vector<int> &x) {return x[0];});
        priority_queue<int, vector<int>, greater<>> idles;
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> occupied;
        vector<int> counter(n, 0);
        for (int i=0;i<n;i++) {
            idles.push(i);
        }
        for (auto &m: meetings) {
            while (occupied.size()&&occupied.top().first<=m[0]) {
                int x=occupied.top().second;
                occupied.pop();
                idles.push(x);
            }
            if (idles.size()) {
                int x=idles.top();
                idles.pop();
                occupied.push({m[1], x});
                counter[x]++;
            }
            else {
                auto pa = occupied.top();
                occupied.pop();
                occupied.push({pa.first+m[1]-m[0], pa.second});
                counter[pa.second]++;
            }
        }
        int mx=0;
        int ans=-1;
        for (int i=0;i<n;i++) {
            if (counter[i]>mx) {
                mx=counter[i];
                ans=i;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto meetings=parseGrid("[[0,10],[1,2],[12,14],[13,15]]");

    Solution so;
    cout << so.mostBooked(2, meetings) << endl;
    return 0;
}
