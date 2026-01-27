#pragma once

#include "lc_pub.h"
 

// 稀疏图：边的数量远小于 n^2的图。
// O(mlogm)  m 为 边数

int dijstra1(vector<vector<int>>& times, int n, int k) {
    vector<vector<pair<int, int>>> g(n); // 邻接表
    for (auto& t : times) {
        g[t[0] - 1].emplace_back(t[1] - 1, t[2]);
    }

    vector<int> dis(n, INT_MAX);
    dis[k - 1] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.emplace(0, k - 1);
    while (!pq.empty()) {
        auto [dx, x] = pq.top();
        pq.pop();
        if (dx > dis[x]) { // x 之前出堆过
            continue;
        }
        for (auto &[y, d] : g[x]) {
            int new_dis = dx + d;
            if (new_dis < dis[y]) {
                dis[y] = new_dis; // 更新 x 的邻居的最短路
                pq.emplace(new_dis, y);
            }
        }
    }
    int mx = ranges::max(dis);
    return mx < INT_MAX ? mx : -1;
}

// 稠密图：边的数量级和 n^2  相当的图。
int dijstra2(vector<vector<int>>& times, int n, int k) {
    vector<vector<int>> g(n, vector<int>(n, INT_MAX / 2)); // 邻接矩阵
    for (auto& t : times) {
        g[t[0] - 1][t[1] - 1] = t[2];
    }

    vector<int> dis(n, INT_MAX / 2), done(n);
    dis[k - 1] = 0;
    while (true) {
        int x = -1;
        for (int i = 0; i < n; i++) {
            if (!done[i] && (x < 0 || dis[i] < dis[x])) {
                x = i;
            }
        }
        if (x < 0) {
            return ranges::max(dis);
        }
        if (dis[x] == INT_MAX / 2) { // 有节点无法到达
            return -1;
        }
        done[x] = true; // 最短路长度已确定（无法变得更小）
        for (int y = 0; y < n; y++) {
            // 更新 x 的邻居的最短路
            dis[y] = min(dis[y], dis[x] + g[x][y]);
        }
    }
}

// 返回从起点 start 到每个点的最短路长度 dis，如果节点 x 不可达，则 dis[x] = LLONG_MAX
// 要求：没有负数边权
// 时间复杂度 O(n + mlogm)，注意堆中有 O(m) 个元素
vector<long long> shortestPathDijkstra(int n, vector<vector<int>>& edges, int start) {
    // 注：如果节点编号从 1 开始（而不是从 0 开始），可以把 n 加一
    vector<vector<pair<int, int>>> g(n); // 邻接表
    for (auto& e : edges) {
        int x = e[0], y = e[1], wt = e[2];
        g[x].emplace_back(y, wt);
        // g[y].emplace_back(x, wt); // 无向图加上这行
    }

    vector<long long> dis(n, LLONG_MAX);
    // 堆中保存 (起点到节点 x 的最短路长度，节点 x)
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    dis[start] = 0; // 起点到自己的距离是 0
    pq.emplace(0, start);

    while (!pq.empty()) {
        auto [dis_x, x] = pq.top();
        pq.pop();
        if (dis_x > dis[x]) { // x 之前出堆过
            continue;
        }
        for (auto& [y, wt] : g[x]) {
            auto new_dis_y = dis_x + wt;
            if (new_dis_y < dis[y]) {
                dis[y] = new_dis_y; // 更新 x 的邻居的最短路
                // 懒更新堆：只插入数据，不更新堆中数据
                // 相同节点可能有多个不同的 new_dis_y，除了最小的 new_dis_y，其余值都会触发上面的 continue
                pq.emplace(new_dis_y, y);
            }
        }
    }

    return dis;
}

