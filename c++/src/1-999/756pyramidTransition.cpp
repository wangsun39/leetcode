#include "lc_pub.h"

using namespace std;

class Solution {
public:
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        unordered_map<string, string> al;
        int n=bottom.size();
        for (auto &x: allowed) {
            al[x.substr(0, 2)]+=x[2];
        }

        string vis[6][6] = {""};
        for (int i=0;i<n;i++) {
            vis[0][i]=bottom[i];
        }

        auto dfs = [&](this auto&& dfs, int r, int c) -> bool {
            string pre=vis[r-1][c]+vis[r-1][c+1];
            if (r == n - 1) return al[pre].size()>0;
            for (string x: al[pre]) {
                vis[r][c]=x;
                if (c == n - r - 1) {
                    if (dfs(r + 1, 0)) return true;
                }
                else {
                    if (dfs(r, c+1)) return true;
                }
            }
            return false;
        };
        return dfs(1, 0);
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[1,3],[3,7],[8,9]]");
    Solution so;
    return 0;
}