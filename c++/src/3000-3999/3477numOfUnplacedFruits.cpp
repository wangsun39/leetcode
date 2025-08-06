#include "lc_pub.h"

template<typename T>
class FenwickTree2 {
    int n;
    vector<T> tree;      // 各节点维护的区间最大值
    vector<T> original;  // 原始数组（1..n）
public:
    FenwickTree2(int n) : n(n), tree(n + 1), original(n + 1) {}

    /* 用给定数组一次性建立树状数组（1-based 下标） */
    void build(const vector<T>& a) {
        for (int i = 1; i <= n; ++i) original[i] = a[i - 1];
        for (int i = 1; i <= n; ++i) {
            int idx = i;
            while (idx <= n) {
                tree[idx] = max(tree[idx], original[i]);
                idx += idx & -idx;
            }
        }
    }

    /* 把 original[pos] 改为 val，并同步更新树状数组 */
    void update(int pos, T val) {
        original[pos] = val;
        while (pos <= n) {
            // 重新计算 tree[pos] 所负责区间 [l, pos] 的最大值
            int l = pos - (pos & -pos) + 1;
            T mx = original[pos];
            for (int i = l; i < pos; ++i) mx = max(mx, original[i]);
            if (tree[pos] == mx) break;   // 没变化，后面的节点也不会变
            tree[pos] = mx;
            pos += pos & -pos;
        }
    }

    /* 查询前缀 [1..r] 的最大值 */
    T query(int r) const {
        T res = numeric_limits<T>::lowest();
        while (r > 0) {
            res = max(res, tree[r]);
            r -= r & -r;
        }
        return res;
    }

    /* 可选：查询整个数组的最大值 */
    T query_all() const { return query(n); }
};

class Solution {
    public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size();
        FenwickTree2<int> fw(n);
        int ans = 0;
        for (int i=0;i<n;i++) {
            fw.update(i+1, baskets[i]);
        }
        for (int i=0;i<n;i++) {
            if (fw.query(n) < fruits[i]) {
                ans++;
                continue;
            }
            if (fw.query(1) >= fruits[i]) {
                fw.update(1, 0);
                continue;
            }
            int lo=1,hi=n;
            while (lo + 1 < hi) {
                int mid = (lo+hi)/2;
                if (fw.query(mid)>=fruits[i]) {
                    hi=mid;
                }
                else {
                    lo=mid;
                }
            }
            fw.update(hi,0);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,6,1}, baskets{6,4,7};

    Solution so;
    cout<<so.numOfUnplacedFruits(nums,baskets)<<endl;
    return 0;
}
