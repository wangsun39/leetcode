#include "lc_pub.h"

class Solution {
    public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        for (int i=0;i<200;i++) {
            bool over=false;
            for (int j=0;j<n;j++) {
                if (strs[j].size()<=i||strs[j][i]!=strs[0][i]) {
                    return strs[0].substr(0, i);
                }
            }
        }
        return strs[0];
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<string> nums = {"flower","flow","flight"};
    Solution so;
    auto v = so.longestCommonPrefix(nums);
    cout << v << endl;
    return 0;
}
