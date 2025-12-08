#include "lc_pub.h"

class Solution {
public:
    int countTriples(int n) {
        unordered_set<int> s;
        for (int i=1;i<n;i++) {
            if (i*i>n) break;
            s.insert(i*i);
        }
        int ans=0;
        for (int i=1;i<n;i++) {
            for (int j=i;j<n;j++) {
                int c=i*i+j*j;
                if (s.find(c)!=s.end()) ans+=2;
            }
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums={1,3};
    Solution so;
    auto v = so.countTriples(50);
    cout << v << endl;
    return 0;
}
