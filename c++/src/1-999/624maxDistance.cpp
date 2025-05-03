#include "lc_pub.h"

using namespace std;

class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int mx = arrays[0][0], mn = arrays[0][0];
        int ans = 0;
        for (int i=0;i<arrays.size() - 1;i++) {
            mn = min(arrays[i].front(), mn);
            mx = max(arrays[i].back(), mx);
            for (int j=0;j<arrays[i+1].size();j++) {
                ans = max({abs(arrays[i+1][j]-mn), abs(arrays[i+1][j]-mx), ans});
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> arrays = parseGrid("[[1,2,3],[4,5],[1,2,3]]");
    Solution so;
    cout << so.maxDistance(arrays) <<endl;
    return 0;
}