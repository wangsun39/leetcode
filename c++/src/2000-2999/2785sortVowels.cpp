#include "lc_pub.h"

class Solution {
    public:
    string sortVowels(string s) {
        int n = s.size();
        string ans = s;
        vector<int> pos;
        vector<char> vowel;
        for (int i=0;i<n;i++) {
            if (s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U') {
                pos.push_back(i);
                vowel.push_back(s[i]);
            }
        }
        ranges::sort(vowel);
        for (int i=0;i<pos.size();i++) {
            ans[pos[i]] = vowel[i];
        }
        return ans;
    }
    };


    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    cout << so.sortVowels("lEetcOde") << endl;
    return 0;
}
