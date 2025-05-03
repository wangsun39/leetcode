#include "lc_pub.h"

template<typename T>
class FenwickTree {
    vector<T> tree;

public:
    // 使用下标 1 到 n
    FenwickTree(int n) : tree(n + 1) {}

    // a[i] 增加 val
    // 1 <= i <= n
    void update(int i, T val) {
        for (; i < tree.size(); i += i & -i) {
            tree[i] += val;
        }
    }

    // 求前缀和 a[1] + ... + a[i]
    // 1 <= i <= n
    T pre(int i) const {
        T res = 0;
        for (; i > 0; i &= i - 1) {
            res += tree[i];
        }
        return res;
    }
};


class Solution {
    public:
    long long goodTriplets(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        vector<int> map(n);
        for (int i=0;i<n;i++) map[nums1[i]] = i;
        FenwickTree<int> fw(n);
        long long ans=0;
        for (int i=0;i<n;i++) {
            int x=map[nums2[i]];
            int v1=fw.pre(map[nums2[i]]+1);  // <i的下标中，比x小的数的个数
            int v2=i-v1;  // <i的下标中，比x大的数的个数
            int v3=n-map[nums2[i]]-1-v2;  // >i的下标中，比x大的数的个数
            ans += (long long)v1 * v3;

            fw.update(map[nums2[i]]+1, 1);
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr = parseGrid("[[3,2],[4,3],[4,4],[2,5]]");
    vector<int> n1{2,0,1,3}, n2{0,1,2,3};

    Solution so;
    cout << so.goodTriplets(n2, n1) << endl;
    return 0;
}
