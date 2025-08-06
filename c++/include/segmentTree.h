#pragma once

#include "lc_pub.h"
 
// 模板来源 https://leetcode.cn/circle/discuss/mOr1u6/
// 线段树有两个下标，一个是线段树节点的下标，另一个是线段树维护的区间的下标
// 节点的下标：从 1 开始，如果你想改成从 0 开始，需要把左右儿子下标分别改成 node*2+1 和 node*2+2
// 区间的下标：从 0 开始
template<typename T>
class SegmentTree {
    // 注：也可以去掉 template<typename T>，改在这里定义 T
    // using T = pair<int, int>;

    int n;
    vector<T> tree;

    // 合并两个 val
    T merge_val(T a, T b) const {
        return max(a, b); // **根据题目修改**
    }

    // 合并左右儿子的 val 到当前节点的 val
    void maintain(int node) {
        tree[node] = merge_val(tree[node * 2], tree[node * 2 + 1]);
    }

    // 用 a 初始化线段树
    // 时间复杂度 O(n)
    void build(const vector<T>& a, int node, int l, int r) {
        if (l == r) { // 叶子
            tree[node] = a[l]; // 初始化叶节点的值
            return;
        }
        int m = (l + r) / 2;
        build(a, node * 2, l, m); // 初始化左子树
        build(a, node * 2 + 1, m + 1, r); // 初始化右子树
        maintain(node);
    }

    void update(int node, int l, int r, int i, T val) {
        if (l == r) { // 叶子（到达目标）
            // 如果想直接替换的话，可以写 tree[node] = val
            tree[node] = merge_val(tree[node], val);
            return;
        }
        int m = (l + r) / 2;
        if (i <= m) { // i 在左子树
            update(node * 2, l, m, i, val);
        } else { // i 在右子树
            update(node * 2 + 1, m + 1, r, i, val);
        }
        maintain(node);
    }

    T query(int node, int l, int r, int ql, int qr) const {
        if (ql <= l && r <= qr) { // 当前子树完全在 [ql, qr] 内
            return tree[node];
        }
        int m = (l + r) / 2;
        if (qr <= m) { // [ql, qr] 在左子树
            return query(node * 2, l, m, ql, qr);
        }
        if (ql > m) { // [ql, qr] 在右子树
            return query(node * 2 + 1, m + 1, r, ql, qr);
        }
        T l_res = query(node * 2, l, m, ql, qr);
        T r_res = query(node * 2 + 1, m + 1, r, ql, qr);
        return merge_val(l_res, r_res);
    }

public:
    // 线段树维护一个长为 n 的数组（下标从 0 到 n-1），元素初始值为 init_val
    SegmentTree(int n, T init_val) : SegmentTree(vector<T>(n, init_val)) {}

    // 线段树维护数组 a
    SegmentTree(const vector<T>& a) : n(a.size()), tree(2 << bit_width(a.size() - 1)) {
        build(a, 1, 0, n - 1);
    }

    // 更新 a[i] 为 merge_val(a[i], val)
    // 时间复杂度 O(log n)
    void update(int i, T val) {
        update(1, 0, n - 1, i, val);
    }

    // 返回用 merge_val 合并所有 a[i] 的计算结果，其中 i 在闭区间 [ql, qr] 中
    // 时间复杂度 O(log n)
    T query(int ql, int qr) const {
        return query(1, 0, n - 1, ql, qr);
    }

    // 获取 a[i] 的值
    // 时间复杂度 O(log n)
    T get(int i) const {
        return query(1, 0, n - 1, i, i);
    }
};

int main() {
    SegmentTree t(8, 0LL); // 如果这里写 0LL，那么 SegmentTree 存储的就是 long long 数据
    t.update(0, 1LL << 60);
    cout << t.query(0, 7) << endl;

    vector<int> nums = {3, 1, 4, 1, 5, 9, 2, 6};
    // 注意：如果要让 SegmentTree 存储 long long 数据，需要传入 vector<long long>
    SegmentTree t2(nums); // 这里 SegmentTree 存储的是 int 数据
    cout << t2.query(0, 7) << endl;
    return 0;
}

