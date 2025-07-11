#include "lc_pub.h"


class Solution {
    public:
    int countDays(int days, vector<vector<int>>& meetings) {
        
        ranges::sort(meetings, [](const vector<int>& a, const vector<int>& b) {
                        if (a[0]==b[0]) return a[1] < b[1];
                        return a[0] < b[0];
                    });
        stack<vector<int>> sk;
        int n=meetings.size();
        for (int i=0;i<n;i++) {
            while (sk.size()>0) {
                if (sk.top()[0] > meetings[i][1]||sk.top()[1]<meetings[i][0]) break;
                meetings[i][0]=min(sk.top()[0], meetings[i][0]);
                meetings[i][1]=max(sk.top()[1], meetings[i][1]);

                sk.pop();
            }
            sk.push(meetings[i]);
        }
        int s = 0;
        while(sk.size()>0) {
            s+=sk.top()[1]-sk.top()[0]+1;
            sk.pop();
        }
        return days-s;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> grid = parseGrid("[[5,7],[1,3],[9,10]]");

    Solution so;
    cout << so.countDays(10,grid) << endl;
    return 0;
}
