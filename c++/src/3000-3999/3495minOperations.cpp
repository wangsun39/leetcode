#include "lc_pub.h"


class Solution {
    public:
    long long minOperations(vector<vector<int>>& queries) {
        int n = queries.size();
        long long ans=0;
        vector<long long>s(1,0);  // 前缀和
        for (int i=0;i<29;i++) {
            s.emplace_back(((1LL<<(i*2))+(1LL<<(i*2+1)))*(i+1)+s[i]);
        }
        for (int i=0;i<n;i++) {
            int l=queries[i][0],r=queries[i][1];
            int li=(__lg(l)+1+1)/2-1,ri=(__lg(r)+1+1)/2-1;  // l和r对应的区间的下标，(下标+1)即一个数需要操作的次数
            if (li==ri) {
                long long c=(long long)(li+1)*(r-l+1);
                ans+=(c+1)/2;
            }
            else {
                long long cl=(1<<(li+1)*2)-l,cr=r-(1<<((ri+1-1)*2))+1;  // l和c所处相同下标的区间内，需要统计的元素个数
                long long c=cl*(li+1)+cr*(ri+1)+(s[ri]-s[li+1]);  // 加上区间和，得到总的操作次数
                ans+=(c+1)/2;
            }
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto grid=parseGrid("[[1,21]]");

    Solution so;
    cout<<so.minOperations(grid)<<endl;
    return 0;
}
