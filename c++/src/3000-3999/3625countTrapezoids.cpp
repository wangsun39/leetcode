#include "lc_pub.h"


class Solution {
    public:
    int countTrapezoids(vector<vector<int>>& points) {
        unordered_map<double, map<double, int>>cnt; // [斜率][截距]: 数量
        unordered_map<int, map<double, int>>cnt2; // [中点][斜率]: 数量
        int n=points.size();
        for (int i=0;i<n;i++) {
            int x=points[i][0],y=points[i][1];
            for (int j=i+1;j<n;j++) {
                int x2=points[j][0],y2=points[j][1];
                int dy=y2-y,dx=x2-x;
                double k=dx?(double)dy/dx:__DBL_MAX__;
                double b=dx?((double)y*dx-x*dy)/dx:x;
                cnt[k][b]++;
                cnt2[((x+x2+2000)<<16)+(y+y2+2000)][k]++;  // 把二维坐标映射到一维上，因为数据范围小
            }
        }
        int ans=0;
        for (auto &[_, cc]: cnt) {
            int s=0;
            for (auto &[_, dd]: cc) {
                ans+=s*dd;
                s+=dd;
            }
        }
        for (auto &[_, cc]: cnt2) {
            int s=0;
            for (auto &[_, dd]: cc) {
                ans-=s*dd;
                s+=dd;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>>q= parseGrid("[[0,0],[1,0],[0,1],[1,1]]");

    Solution so;
    cout<<so.countTrapezoids(q)<<endl;
    return 0;
}
