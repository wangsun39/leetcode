#include "lc_pub.h"

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        // priority_queue<int, vector<int>, greater<vector<int>>> pq;
        int dir[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        int r=heightMap.size(),c=heightMap[0].size();
        vector<vector<int>> vis(r, vector<int>(c, 0));
        for (int i=0;i<c;i++) {
            pq.push({heightMap[0][i],0,i});
            pq.push({heightMap[r-1][i],r-1,i});
            vis[0][i]=1;vis[r-1][i]=1;
        }
        for (int i=1;i<r-1;i++) {
            pq.push({heightMap[i][0],i,0});
            pq.push({heightMap[i][c-1],i,c-1});
            vis[i][0]=vis[i][c-1]=1;
        }
        int ans=0;
        while (pq.size()) {
            auto e=pq.top();
            pq.pop();
            int h=e[0],x=e[1],y=e[2];
            // auto [v,x,y]=pq.top();
            for (int i=0;i<4;i++) {
                auto [dx,dy]=dir[i];
                int u=x+dx,v=y+dy;
        // cout<<"A"<<u<<v<<r<<c<<endl;
                if (0<=u&&u<r&&0<=v&&v<c&&!vis[u][v]) {
                    if (heightMap[u][v]<=h) {
                        pq.push({h,u,v});
                        ans+=(h-heightMap[u][v]);
                    }
                    else pq.push({heightMap[u][v],u,v});
                    vis[u][v]=1;
                }
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3};
    Solution so;
    return 0;
}
