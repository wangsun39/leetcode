#include "lc_pub.h"

bool vis[50000]={0};
class Solution {
private:
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        ranges::sort(meetings, {}, [&](vector<int> &a) {return a[2];});
        // vector<int>vis(n, 0);
        memset(vis,0,n);
        vis[0]=vis[firstPerson]=1;
        map<int, vector<pair<int, int>>> mip;
        int m=meetings.size();
        int cur=meetings[0][2];
        for (int i=0;i<m;) {
            deque<int> dq;
            unordered_map<int, vector<int>> g;
            
            while (i<m&&meetings[i][2]==cur) {
                g[meetings[i][0]].push_back(meetings[i][1]);
                g[meetings[i][1]].push_back(meetings[i][0]);
                i++;
            }
            if (i<m) cur=meetings[i][2];
            for (auto &[uk, uv]: g) {
                if (vis[uk]) dq.push_back(uk);
            }
            while (dq.size()) {
                int x=*dq.begin();
                dq.pop_front();
                for (int y: g[x]) {
                    if (vis[y]==0) {
                        dq.push_back(y);
                        vis[y] = 1;
                    }
                }
            }
        }
        vector<int> ans;
        for (int i=0;i<n;i++) {
            if (vis[i]) ans.push_back(i);
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[3,1,3],[1,2,2],[0,3,3]]");

    Solution so;
    cout << so.findAllPeople(4,arr,3) << endl;
    return 0;
}
