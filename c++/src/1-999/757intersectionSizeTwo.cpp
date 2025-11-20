#include "lc_pub.h"

using namespace std;

class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        int n = intervals.size();
        int mx_l=0,mn_r=INT_MAX;
        for (auto & inter: intervals) {
            int l=inter[0],r=inter[1];
            mx_l=max(mx_l,l);
            mn_r=min(mn_r,r);
        }
        if (mx_l>=mn_r) {
            return mx_l + 1 - (mn_r - 1) + 1;
        }
        int cl=0,cr=0;
        for (auto & inter: intervals) {
            int l=inter[0],r=inter[1];
            if (l==mx_l)cl++;
            if (r=mn_r)cr++;
        }
        if (cl>1&&cr>1) return 3;
        return 2;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[1,3],[3,7],[8,9]]");
    Solution so;
    cout<<so.intersectionSizeTwo(arr)<<endl;
    return 0;
}