#include "lc_pub.h"


class Solution {
    public:
    long long countGoodIntegers(int n, int k) {
        vector<int> factorial(n + 1);
        factorial[0] = 1;
        for (int i = 1; i <= n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }

        // 回文一半的长度范围
        int len=(n+1)/2;
        int lo=pow(10, len-1),hi=pow(10,len);
        int m=0;
        if (n&1) m=pow(10, len-1);
        else m=pow(10,len);
        unordered_set<string> vis;  // 记录已经处理过的数字
        long long ans=0;
        for (int i=lo;i<hi;i++) {
            // 枚举一半长度为i的回文
            string s1 = to_string(i);
            string s2;
            if(n&1) {
                s2 = string(s1.rbegin()+1, s1.rend());  // 翻转字符串
            }
            else {
                s2 = string(s1.rbegin(), s1.rend());
            }
            string s=s1+s2;
            if (stoull(s)%k!=0) continue;
            ranges::sort(s);  // 排序字符串
            if (vis.find(s)!=vis.end()) continue;
            vis.emplace(s);
            unordered_map<char, int> counter;
            for (auto x: s) counter[x]++;
            long long v = (n-counter['0']) * factorial[n-1];
            for (auto x :counter) {
                v /= factorial[x.second];
            }
            ans+=v;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{5,2,5,4,5};

    Solution so;
    cout << so.countGoodIntegers(3, 5) << endl;
    cout << so.countGoodIntegers(1, 4) << endl;
    return 0;
}
