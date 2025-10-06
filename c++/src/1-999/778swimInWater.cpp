#include "lc_pub.h"

using namespace std;

class UnionFind {
    vector<int> fa; // 代表元
    vector<int> sz; // 集合大小

public:
    int cc; // 连通块个数

    UnionFind(int n) : fa(n), sz(n, 1), cc(n) {
        // 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        // 集合 i 的代表元是自己，大小为 1
        ranges::iota(fa, 0); // iota(fa.begin(), fa.end(), 0);
    }

    // 返回 x 所在集合的代表元
    // 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    int find(int x) {
        // 如果 fa[x] == x，则表示 x 是代表元
        if (fa[x] != x) {
            fa[x] = find(fa[x]); // fa 改成代表元
        }
        return fa[x];
    }

    // 判断 x 和 y 是否在同一个集合
    bool is_same(int x, int y) {
        // 如果 x 的代表元和 y 的代表元相同，那么 x 和 y 就在同一个集合
        // 这就是代表元的作用：用来快速判断两个元素是否在同一个集合
        return find(x) == find(y);
    }

    // 把 from 所在集合合并到 to 所在集合中
    // 返回是否合并成功
    bool merge(int from, int to) {
        int x = find(from), y = find(to);
        if (x == y) { // from 和 to 在同一个集合，不做合并
            return false;
        }
        fa[x] = y; // 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        sz[y] += sz[x]; // 更新集合大小（注意集合大小保存在代表元上）
        // 无需更新 sz[x]，因为我们不用 sz[x] 而是用 sz[find(x)] 获取集合大小，但 find(x) == y，我们不会再访问 sz[x]
        cc--; // 成功合并，连通块个数减一
        return true;
    }

    // 返回 x 所在集合的大小
    int get_size(int x) {
        return sz[find(x)]; // 集合大小保存在代表元上
    }
};

class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int dir[4][2] = {{0, 1},{1,0},{0,-1},{-1,0}};
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        int r=grid.size(),c=grid[0].size();
        UnionFind uf(r * c);
        unordered_set<int> vis;
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                pq.push({grid[i][j],i,j});
                
                // for (int k=0;k<4;k++) {
                //     auto [dx, dy] = dir[k];
                //     int x=i+dx,y=j+dy;
                //     if (0<=x&&x<r&&0<=y&&y<c&&vis.find(x*c+y)!=vis.end())
                //         uf.merge(i*c+j,x*c+y);
                // }
            }
        }
        while (true) {
            auto& arr = pq.top();
            int ans=arr[0], i=arr[1], j=arr[2];
            for (int k=0;k<4;k++) {
                auto [dx, dy] = dir[k];
                int x=i+dx,y=j+dy;
                if (0<=x&&x<r&&0<=y&&y<c&&vis.find(x*c+y)!=vis.end())
                    uf.merge(i*c+j,x*c+y);
            }
            vis.insert(i * c + j);
            pq.pop();
            
            if (uf.find(0)==uf.find(r*c-1)) return ans;
        }

    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[0,2],[1,3]]");
    Solution so;
    cout << so.swimInWater(arr) <<endl;
    return 0;
}