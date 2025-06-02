#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
    
    public:
    int candy(vector<int>& ratings) {
        int n= ratings.size();
        int ans=0;
        vector<int>left(n,0),right(n,0);
        for(int i=1;i<n;i++) {
            if (ratings[i-1]<ratings[i]) {
                left[i]=left[i-1]+1;
            }
        }
        for (int i=n-1;i>=1;i--) {
            if (ratings[i-1]>ratings[i]) {
                right[i-1]=right[i]+1;
            }
        }
        for (int i=0;i<n;i++) {
            ans += max(left[i], right[i]);
        }
        return ans+n;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int>ratings{1,3,4,5,2};

    Solution so;
    auto v = so.candy(ratings);
    // auto v = so.minCut("ababababababababababababcbabababababababababababa");
    cout << v << endl;
    return 0;
}
