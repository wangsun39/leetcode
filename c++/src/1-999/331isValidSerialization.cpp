#include "lc_pub.h"


// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
public:
bool isValidSerialization(string preorder) {
    if(preorder=="#") return true;
    stack<int> stk;
    int n = preorder.size();
    for (int i=0;i<n;i++) {
        if(preorder[i]==',') continue;
        if(preorder[i]=='#') {
            if (stk.size()==0) return false;
            while(stk.size()) {
                if(stk.top()==2) stk.pop();
                else {stk.top()=2;break;}
            }
            if (stk.size()==0) return i==n-1;
        }
        else {
            if (i==0||preorder[i-1]==',') stk.push(1);
            else continue;
        }
    }
    return stk.size()==0;
}
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    auto v = so.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#");
    cout << v << endl;
    return 0;
}
