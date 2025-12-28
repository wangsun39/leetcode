#include "lc_pub.h"


class Solution {
    
    public:
    int countNegatives(vector<vector<int>>& grid) {
        int r=grid.size(),c=grid[0].size();
        int pos=c-1;
        int ans=0;
        for (int i=0;i<r;i++) {
            while (pos>=0&&grid[i][pos]<0) {
                pos--;
            }
            ans+=c-pos-1;
        }
        return ans;
    }
};
struct Compare {
    bool operator()(int a, int b) const {
        return a > b; // 返回 true 表示 b 的优先级更高
    }
};
int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[1,10],[1,2],[2,3],[2,2],[2,5]]");
    Solution so;

    return 0;
}
