#include "lc_pub.h"

class Solution {
    public:
    int countSymmetricIntegers(int low, int high) {
        auto check = [](string s) -> bool {
            int n=s.size();
            int l=0,r=0;
            for (int i=0;i<n/2;i++) l+=s[i] - '0';
            for (int i=n/2;i<n;i++) r+=s[i] - '0';
            return l==r;
        };
        int ans=0;
        for (int i=low;i<=high;i++) {
            string s=to_string(i);
            if ((s.size() & 1) == 0) {
                if (check(s)) ans++;
            }
        }
        return ans;
    }
    };

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    cout << so.countSymmetricIntegers(1,100) << endl;
    return 0;
}
