#include "lc_pub.h"

class Solution {
public:
    
    int findKthNumber(int n, int k) {
        string sn = to_string(n);
        int m = sn.size();

        // 建立 10 叉树，根节点编号0，后面的数字依次编号，前序遍历此树

        auto calc = [&](int node) -> int {
            // 计算node节点的子节点数量
            string s_node = to_string(node);
            int len = s_node.size();
            int cnt=0;
            if (sn.starts_with(s_node)) {                
                for (int i=0;i<m-len;i++) {
                    cnt=cnt*10+1;
                }
                cnt+=n%int(pow(10,m-len))+1;
            }
            else {
                if (sn.substr(0,len) > s_node) {
                    for (int i=0;i<m-len+1;i++) {
                        cnt=cnt*10+1;
                    }
                }
                else {
                    for (int i=0;i<m-len;i++) {
                        cnt=cnt*10+1;
                    }
                }
                
            }
            return cnt;
        };

        int ans = 0;

        int node = 1;
        while (k > 0) {
            int v = calc(node);
            if (v < k) {
                node ++;  // 找兄弟节点
                k-=v;
            }
            else {
                if (k==1) return node;
                k--;
                node *= 10;  // 找子节点
            }
        }
        return node;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{1,2,3};
    Solution so;
    auto v = so.findKthNumber(100, 10);
    cout << v << endl;
    return 0;
}
