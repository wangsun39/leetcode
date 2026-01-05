#include "lc_pub.h"

class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        int n=matrix.size();
        long long ans=0;
        int mn=INT_MAX;
        int cnt=0;
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                if (matrix[i][j]<0) {
                    cnt++;
                }
                mn=min(mn,abs(matrix[i][j]));
                ans+=abs(matrix[i][j]);
            }
        }
        if (cnt&1) return ans-mn*2;
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,3};
    // vector<vector<int>> grid = parseGrid("[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]");
    // cout << grid.size() << "  " << grid[0].size()<< endl;

    Solution so;
    return 0;
}
