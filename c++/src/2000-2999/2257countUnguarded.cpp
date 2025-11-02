#include "lc_pub.h"

class RangeFreqQuery {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<pair<int, int>>> row(m);
        vector<vector<pair<int, int>>> col(n);
        unordered_set<int> picked;
        for (auto &p: guards) {
            row[p[0]].push_back({p[1], 0});
            col[p[1]].push_back({p[0], 0});
        }
        for (auto &p: walls) {
            row[p[0]].push_back({p[1], 1});
            col[p[1]].push_back({p[0], 1});
        }
        for (int k=0;k<m;k++) {
            auto &r= row[k];
            r.push_back({-1,1});
            r.push_back({n,1});
            ranges::sort(r);
            int sz=r.size();
            for (int i=0;i<sz-1;i++) {
                if (r[i].second==1&&r[i+1].second==1) {
                    for (int j=r[i].first+1;j<r[i+1].first;j++) {
                        picked.insert(k*n+j);
                    }
                }
            }
        }
        int ans=0;
        for (int k=0;k<n;k++) {
            auto &c= col[k];
            c.push_back({-1,1});
            c.push_back({m,1});
            ranges::sort(c);
            int sz=c.size();
            for (int i=0;i<sz-1;i++) {
                if (c[i].second==1&&c[i+1].second==1) {
                    for (int j=c[i].first+1;j<c[i+1].first;j++) {
                        if (picked.find(j*n+k)!=picked.end()) ans++;
                    }
                }
            }
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<string> arr = {"a","b","c","ab","bc","abc"};
    vector<vector<int>> guards=parseGrid("[[1,5],[1,1],[1,6],[0,2]]");
    vector<vector<int>> walls=parseGrid("[[0,6],[0,3],[0,5]]");

    RangeFreqQuery so;
    cout << so.countUnguarded(2,7,guards,walls) << endl;
    return 0;
}
