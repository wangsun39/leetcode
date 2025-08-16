#include "lc_pub.h"


class Solution {
    
    public:
    int maximum69Number (int num) {
        int arr[5];
        for (int i=0;i<5;i++) {
            arr[i] = num % 10;
            num /= 10;
        }
        for (int i=5;i>=0;i--)
            if (arr[i]==6) {
                arr[i]=9;
                break;
            }
        int ans=0;
        for (int i=5;i>=0;i--)
            ans = ans * 10 + arr[i];
        
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[1,10],[1,2],[2,3],[2,2],[2,5]]");
    Solution so;
    cout<<so.maximum69Number(9669)<<endl;
    return 0;
}
