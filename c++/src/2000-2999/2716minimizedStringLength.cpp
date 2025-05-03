#include "lc_pub.h"

class Solution {
    public:
        int minimizedStringLength(string s) {
            unordered_map<char, int> counter;
            int n = s.size();
            for(int i=0;i<n;i++) {
                counter[s[i]]++;
            }
            return counter.size();
            // return unordered_set(s.begin(), s.end()).size();
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
    cout << so.minimizedStringLength("cbbd") << endl;
    return 0;
}
