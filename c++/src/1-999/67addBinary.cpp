#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        string ans="";
        int carry=0,i=a.size()-1,j=b.size()-1;
        while (i>=0||j>=0||carry) {
            int n1=0,n2=0;
            if (i>=0) n1=a[i]-'0';
            if (j>=0) n2=b[j]-'0';
            if (n1^n2) {
                if (carry) ans='0'+ans;
                else ans='1'+ans;
            }
            else {
                if (carry) {ans='1'+ans;}
                else ans ='0'+ans;
                carry=n1&n2;
            }
            i--;j--;
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    cout<<so.addBinary("11","1");
    return 0;
}