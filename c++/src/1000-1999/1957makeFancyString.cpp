#include "lc_pub.h"

class Solution {
public:
    string makeFancyString(string s) {
        string ans = "";
        int cnt = 0;
        int n = s.size();
        for (int i=0;i<n;i++) {
            if (i > 0 && s[i]==s[i-1]) cnt++;
            else cnt=1;
            if (cnt<3) ans.push_back(s[i]);
        }
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
    auto v = so.makeFancyString("leeetcode");
    cout << v << endl;
    return 0;
}
