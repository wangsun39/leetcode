#include "lc_pub.h"

class Solution {
    public:
    int countOperations(int num1, int num2) {
        int ans=0;
        while(num1&&num2) {
            if (num1>num2) swap(num1,num2);
            ans+=num2/num1;
            num2=num2%num1;
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {3,1,2};

    Solution so;
    cout << so.countOperations(2,3) << endl;
    return 0;
}
