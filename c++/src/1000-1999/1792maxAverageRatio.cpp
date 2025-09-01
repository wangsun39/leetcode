#include "lc_pub.h"

class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        using DII = tuple<double, int, int>;
        auto cmp = [](const DII& a, const DII& b) {
            return get<0>(a) < get<0>(b);
        };
        priority_queue<DII, vector<DII>, decltype(cmp)> pq;  // 大顶堆
        for (auto &c: classes) {
            pq.emplace((c[0] + 1) * 1.0 / (c[1] + 1) - c[0]*1.0/c[1], c[0], c[1]);
        }
        for (int _=0;_<extraStudents;_++) {
            auto [__,p, t] = pq.top();
            p++,t++;
            pq.pop();
            pq.emplace((p+1)*1.0/(t+1)-p*1.0/t,p,t);
        }

        double s = 0.0;
        int n=classes.size();
        for (int _=0;_<n;_++) {
            auto [__,p,t]=pq.top();
            s+=p*1.0/t;
            pq.pop();
        }
        return s/n;

    }
private:
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
