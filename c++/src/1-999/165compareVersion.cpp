#include "lc_pub.h"

// 用了两种lambda递归函数的写法，一种带this，不能引用成员变量，另一种不带this，能引用成员变量

class Solution {
    
    public:
    int compareVersion(string version1, string version2) {
        version1 += ". ", version2+=". ";
        size_t p1=version1.find('.'),p2=version2.find('.');
        size_t pre1=0,pre2=0;
        int n1,n2;
        int m1=version1.size(),m2=version2.size();
        while (p1 != std::string::npos && p2 != std::string::npos) {
            n1=stoi(version1.substr(pre1, p1-pre1));
            n2=stoi(version2.substr(pre2, p2-pre2));
            cout<<n1<<","<<n2<<","<<m1<<","<<m2<<endl;
            if (n1 < n2) return -1;
            if (n1 > n2) return 1;
            pre1=p1+1;pre2=p2+1;
            if (p1==m1-1||p2==m2-1) break;
            p1=version1.find('.',p1+1),p2=version2.find('.',p2+1);
            cout<<p1<<endl;
            cout<<p2<<endl;
        }
        while (p1 != std::string::npos)
        {
            n1=stoi(version1.substr(pre1, p1-pre1));
            if (n1 > 0) return 1;
            pre1=p1+1;
            p1=version1.find('.',p1+1);
            if (p1==m1-1) break;
        }
        while (p2 != std::string::npos)
        {
            n2=stoi(version2.substr(pre2, p2-pre2));
            if (n2 > 0) return -1;
            pre2=p2+1;
            p2=version2.find('.',p2+1);
            if (p2==m2-1) break;
        }
        return 0;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int>ratings{1,3,4,5,2};

    Solution so;
    auto v = so.compareVersion("2.1", "2.2");
    // auto v = so.minCut("ababababababababababababcbabababababababababababa");
    cout << v << endl;
    return 0;
}
