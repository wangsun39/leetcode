#include "lc_pub.h"

using namespace std;

class Solution {
public:

    double largestTriangleArea(vector<vector<int>>& points) {
        int n = points.size();
        auto calc = [](vector<vector<int>>& ps) {
            double x=pow(pow((double)ps[0][0]-ps[1][0],2)+pow(ps[0][1]-ps[1][1],2),0.5);
            double y=pow(pow((double)ps[2][0]-ps[1][0],2)+pow(ps[2][1]-ps[1][1],2),0.5);
            double z=pow(pow((double)ps[0][0]-ps[2][0],2)+pow(ps[0][1]-ps[2][1],2),0.5);
            double p=(x+y+z)/2;
            return pow(p*(p-x)*(p-y)*(p-z),0.5);
        };
        double ans=0;
        for (int i=0;i<n;i++) {
            for (int j=i+1;j<n;j++) {
                for (int k=j+1;k<n;k++) {
                    vector<vector<int>> tri{points[i],points[j],points[k]};
                    ans = max(ans, calc(tri));
                }
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays = {1,1,2};
    Solution so;
    return 0;
}