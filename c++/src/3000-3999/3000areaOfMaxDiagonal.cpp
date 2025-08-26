#include "lc_pub.h"


class Solution {
    public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        long long diag=0;
        long long area=0;
        int n=dimensions.size();
        for (int i=0;i<n;i++) {
            long long x=dimensions[i][0]*dimensions[i][0]+dimensions[i][1]*dimensions[i][1];
            if (diag < x) {
                diag=x;
                area=dimensions[i][0]*dimensions[i][1];
            }
            else if (diag==x&&area<dimensions[i][0]*dimensions[i][1]) {
                area=dimensions[i][0]*dimensions[i][1];
            }
        }
        return area;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,3,3};

    Solution so;
    return 0;
}
