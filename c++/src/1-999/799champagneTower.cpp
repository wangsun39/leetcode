#include "lc_pub.h"

using namespace std;

class Solution {
public:

    double champagneTower(int poured, int query_row, int query_glass) {
        vector<double>dp1(101,0);
        dp1[0]=poured;
        for (int i=1;i<=query_row;i++) {
            vector<double> dp2(101,0);
            for (int j=0;j<=query_glass+1;j++) {
                if (dp1[j]>1) dp2[j]+=(dp1[j]-1)/2;
                if (j&&dp1[j-1]>1) dp2[j]+=(dp1[j-1]-1)/2;
            }
            swap(dp1,dp2);
        }
        return min<double>(1.0, dp1[query_glass]);
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    cout << so.champagneTower(1,1,1) <<endl;
    return 0;
}