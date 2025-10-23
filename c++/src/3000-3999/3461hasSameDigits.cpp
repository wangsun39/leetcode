#include "lc_pub.h"


class Solution {
    public:
    bool hasSameDigits(string s) {
        int n = s.size();
        vector<int> arr(n, 0);
        for (int i=0;i<n;i++) {
            arr[i]=s[i]-'0';
        }
        for (int i=0;i<n-2;i++) {
            for (int j=0;j<n-i-1;j++) {
                arr[j]=(arr[j]+arr[j+1])%10;
            }
        }
        return arr[0]==arr[1];
    }
    
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    cout<<so.hasSameDigits("3902")<<endl;
    return 0;
}
