#include "lc_pub.h"

class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        int n=s.size();
        vector<int> flg(n, 0);
        int i=0;
        b = n - b; // 改为左轮转
        string ans=s;
        while (true) {
            int start = b * i % n;
            if (flg[start]) break;
            string ss=s.substr(start, n-start) + s.substr(0, start);
            int cnt = calc(ss[1]-'0', a);
            for (int i=1;i<n;i+=2) {
                int v=ss[i]-'0';
                ss[i]='0'+(v+cnt*a)%10;
            }
            if (b & 1) {
                int cnt0 = calc(ss[0]-'0', a);
                for (int i=0;i<n;i+=2) {
                    int v=ss[i]-'0';
                    ss[i]='0'+(v+cnt0*a)%10;
                }
            }
            if (ss < ans) ans = ss;
            flg[start]=1;
            i++;
        }
        return ans;
    }
private:
    int calc(int n1, int n2) {
        // 对n1不断累加n2,加多少次能达到最小值
        int res=0,mn=10;
        int flag[10] = {0};
        int i=0;
        while (true) {
            int v = (n1 + n2*i) % 10;
            if (v < mn) {
                mn = v;
                res = i;
            }
            if (flag[v]) return res;
            i++;
            flag[v] = 1;
        }
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<int> p = {1,2,3,4,7};
    Solution so;
    auto v = so.findLexSmallestString("5525", 9,2);
    cout << v << endl;
    return 0;
}
