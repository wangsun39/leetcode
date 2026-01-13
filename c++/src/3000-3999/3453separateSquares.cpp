#include "lc_pub.h"


class Solution {
    public:
    double separateSquares(vector<vector<int>>& squares) {
        double lo=INT_MAX, hi=INT_MIN;
        double s=0;
        for (auto &sq: squares) {
            lo=min(lo, (double)sq[1]);
            hi=max(hi, (double)sq[1]+sq[2]);
            s+=(double)sq[2]*sq[2];
        }

        auto check=[&](double y) -> bool {
            // 纵坐标大于y的面积和，是否<=总面积的一半
            double ss = 0;
            for (auto &sq: squares) {
                if (sq[1]>=y)
                    ss += (double)sq[2] * sq[2];
                else if (sq[1]+sq[2]>=y)
                    ss += (double)sq[2] * (sq[1]+sq[2]-y);
                if (ss*2>s) return false;
            }
            return true;
        };
        while (hi - lo > 1e-6) {
            double mid = (hi+lo)/2;
            if (check(mid))
                hi=mid;
            else
                lo=mid;
        }
        return hi;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> squares{{23,29,3},{28,29,4}};

    Solution so;
    cout<<so.separateSquares(squares)<<endl;
    return 0;
}
