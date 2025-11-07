#include "lc_pub.h"


class Solution {
    public:
    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        unordered_map<int, vector<int>> g;
        for (int i=0;i<connections.size();i++) {
            int x=connections[i][0]-1,y=connections[i][1]-1;
            g[x].push_back(y);
            g[y].push_back(x);
        }
        unordered_map<int, int> gr;
        vector<int>vis(c, 0);
        vector<deque<int>> n_deq;
        for (int i=0;i<c;i++) {
            if (vis[i]) continue;
            deque<int> dq{i};
            vector<int> v2;
            vis[i]=1;
            v2.push_back(i);
            while (dq.size()) {
                int x=dq[0];
                dq.pop_front();
                for (int y: g[x]) {
                    if (!vis[y]) {
                        dq.push_back(y);
                        vis[y]=1;
                        v2.push_back(y);
                    }
                }
            }
            int j=n_deq.size();
            n_deq.push_back({});
            for (int x: v2) {
                gr[x]=j;
                n_deq[j].push_back(x);
            }
            ranges::sort(n_deq[j]);
        }
        vector<int> del(c, 0);
        vector<int> ans;
        for (int i=0;i<queries.size();i++) {
            if (queries[i][0]==1) {
                if (!del[queries[i][1]-1]) {
                    ans.push_back(queries[i][1]);
                    continue;
                }
                int j=gr[queries[i][1]-1];
                while (n_deq[j].size()&&del[n_deq[j][0]]) {
                    n_deq[j].pop_front();
                }
                if (n_deq[j].size()) ans.push_back(n_deq[j][0]+1);
                else ans.push_back(-1);
            }
            else {
                del[queries[i][1]-1]=1;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>>connections= parseGrid("[[1,2],[2,3],[3,4],[4,5]]");
    vector<vector<int>>q= parseGrid("[[1,3],[2,1],[1,1],[2,2],[1,2]]");

    Solution so;
    cout<<so.processQueries(5,connections,q)<<endl;
    return 0;
}
