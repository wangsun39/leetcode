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

