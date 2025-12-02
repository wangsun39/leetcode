#include "lc_pub.h"


class Solution {
    public:
    int countTrapezoids(vector<vector<int>>& points) {
        int MOD=1'000'000'007;
        unordered_map<int, long long> rows;  // 每行的点数
        for (auto &p: points) {
            rows[p[1]]++;
            rows[p[1]];
        }
        int nr=rows.size();
        long long s=0;
        vector<long long> segs;
        for (auto [k,v]: rows) {
            long long x=v*(v-1)/2;
            segs.push_back(x);
            s+=x;
        }
        long long ans=0;
        for (auto x: segs) {
            ans+=x*(s-x);
        }
        return ans/2%MOD;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>>connections= parseGrid("[[1,2],[2,3],[3,4],[4,5]]");
    vector<vector<int>>q= parseGrid("[[0,0],[1,0],[0,1],[2,1]]");

    Solution so;
    cout<<so.countTrapezoids(q)<<endl;
    return 0;
}
