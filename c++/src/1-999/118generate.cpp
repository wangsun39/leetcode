#include "lc_pub.h"



class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<int> a(1, 1);
        vector<int> b;
        vector<vector<int>> ans;
        ans.push_back(a);
        for (int i=0;i<numRows-1;i++) {
            vector<int> b(1,1);
            for (int j=0;j<i;j++) {
                b.push_back(ans[i][j]+ans[i][j+1]);
            }
            b.push_back(1);
            ans.push_back(b);
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    auto v = so.generate(2);
    cout << v << endl;
    return 0;
}
