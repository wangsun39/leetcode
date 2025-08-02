#include "lc_pub.h"

class Solution {
    public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        map<int, int> c1, c2,c;
        long long ans=0;
        for (auto x: basket1) {c1[x]++;c[x]++;}
        for (auto x: basket2) {c2[x]++;c[x]++;}
        int cnt=0;//总的交换次数
        for (auto [k,v]: c) {
            if (v&1) return -1;
            cnt += abs(v/2-c1[k]);
        }
        int mn=(c.begin()->first)*2;
        cnt/=2;
        int cnt1=0;//执行的交换次数
        for (auto [k,v]: c) {
            if (cnt1==cnt) break;
            int v1=abs(v/2-c1[k]);
            if (cnt1+v1<cnt) {
                ans+=v1*min(k,mn);
                cnt1+=v1;
            }
            else {
                ans+=min(k,mn)*(cnt-cnt1);
                break;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr1 = {84,80,43,8,80,88,43,14,100,88},arr2={32,32,42,68,68,100,42,84,14,8};

    Solution so;
    cout << so.minCost(arr1, arr2) << endl;
    return 0;
}
