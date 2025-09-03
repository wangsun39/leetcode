#include "lc_pub.h"


class Solution {
    public:
    int numberOfPairs(vector<vector<int>>& points) {
        int ans=0;
        ranges::sort(points, [](vector<int> &a, vector<int> &b) {
                                if (a[0] != b[0]) return a[0] < b[0];
                                return a[1] > b[1];
                            });
        int n=points.size();
        for (int i=0;i<n;i++) {
            int mn_y=INT_MIN;
            for (int j=i+1;j<n;j++) {
                if (mn_y<points[j][1]&&points[j][1]<=points[i][1]) {
                    ans++;
                    mn_y=points[j][1];
                }
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto points = parseGrid("[[1,1],[2,2],[3,3]]");

    Solution so;
    cout << so.numberOfPairs(points) << endl;
    return 0;
}
