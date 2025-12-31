#include "lc_pub.h"

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
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        vector<pair<int, int>> dir={{1,0},{-1,0},{0,1},{0,-1}};
        int n = row*col;
        vector<vector<int>> grid(row, vector<int>(col, 1));
        UnionFind uf(n);
        for (int j=1;j<col;j++) {
            uf.merge(j-1,j);
            uf.merge((row-1)*col+j-1,(row-1)*col+j);
        }
        int m = cells.size();
        for (int i=m - 1;i>=0;i--) {
            int x=cells[i][0]-1,y=cells[i][1]-1;
            int z1=x*col+y;
            grid[x][y]=0;
            for (auto [dx,dy]: dir) {
                int u=x+dx,v=y+dy;
                if (0<=u&&u<row&&0<=v&&v<col&&grid[u][v]==0) {
                    int z2=u*col+v;
                    uf.merge(z1,z2);
                }
            }
            if (uf.is_same(0, n-1)) return i;
        }
        return 0;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,3};
    // vector<vector<int>> grid = parseGrid("[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]");
    // cout << grid.size() << "  " << grid[0].size()<< endl;

    Solution so;
    return 0;
}
