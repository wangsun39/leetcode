#include "lc_pub.h"

class Solution {
public:
    int maximumGain(string s, int x, int y) {
        if (x < y) {
            for (auto &u: s) {
                if (u=='a') u='b';
                else if (u=='b') u='a';
            }
            swap(x,y);
        }
        int ca=0,cb=0,ans=0;
        for (auto u: s) {
            if (u!='a'&&u!='b') {
                ans+=min(ca,cb)*y;
                ca=cb=0;
            }
            else if(u=='b') {
                if (ca) {
                    ans+=x;
                    ca--;
                }
                else cb++;
            }
            else {
                ca++;
            }
        }
        ans+=min(ca,cb)*y;
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    // vector<vector<int>> grid = {{1,1,1,-1,-1},{1,1,1,-1,-1},{-1,-1,-1,1,1},{1,1,1,1,-1},{-1,-1,-1,-1,-1}};
    vector<vector<int>> grid = parseGrid("[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]");
    cout << grid.size() << "  " << grid[0].size()<< endl;

    Solution so;
    auto v = so.maximumGain("cdbcbbaaabab",4,5);
    cout << v << endl;
    return 0;
}
