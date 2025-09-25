#include "lc_pub.h"



class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n=triangle.size();
        vector<int>dp(n, 0);
        for (int i=n-2;i>=0;i--) {
            for (int j=0;j<=i;j++) {
                triangle[i][j]+=min(triangle[i+1][j], triangle[i+1][j+1]);
            }
        }
        return triangle[0][0];
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
