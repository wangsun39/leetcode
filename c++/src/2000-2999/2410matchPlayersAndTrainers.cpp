#include "lc_pub.h"

class Solution {
    public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        ranges::sort(players);
        ranges::sort(trainers);
        int n=players.size(),m=trainers.size();
        int i = 0;
        int ans=0;
        for (int j=0;j<m;j++) {
           if (players[i]>trainers[j]) continue;
            ans++;
            if (++i>=n) break;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {4,7,9}, t{8,2,5,8};

    Solution so;
    cout << so.matchPlayersAndTrainers(arr,t) << endl;
    return 0;
}
