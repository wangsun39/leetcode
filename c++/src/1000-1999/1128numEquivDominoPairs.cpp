#include "lc_pub.h"

using namespace std;

class Solution {
public:
int numEquivDominoPairs(vector<vector<int>>& dominoes) {
    unordered_map<long long,int>counter;
    int ans=0;
    for (auto &dom: dominoes) {
        if (counter.find((dom[0] << 16) + dom[1])!=counter.end()) {
            ans += counter[(dom[0] << 16) + dom[1]];
            counter[(dom[0] << 16) + dom[1]]++;
        }
        else {
            ans += counter[(dom[1] << 16) + dom[0]];
            counter[(dom[1] << 16) + dom[0]]++;
        }
    }
    return ans;
}
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> arrays = parseGrid("[[2,1],[5,4],[3,7],[6,2],[4,4],[1,8],[9,6],[5,3],[7,4],[1,9],[1,1],[6,6],[9,6],[1,3],[9,7],[4,7],[5,1],[6,5],[1,6],[6,1],[1,8],[7,2],[2,4],[1,6],[3,1],[3,9],[3,7],[9,1],[1,9],[8,9]]");
    Solution so;
    std::cout<<so.numEquivDominoPairs(arrays)<<endl;
    return 0;
}