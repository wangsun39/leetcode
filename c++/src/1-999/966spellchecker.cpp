#include "lc_pub.h"

using namespace std;

class Solution {
    public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        auto s1 = unordered_set(wordlist.begin(), wordlist.end());
        unordered_map<string, string>s2;
        unordered_map<string, string>s3;
        for (auto word: wordlist) {
            string lo = word;
            for (auto &c : lo) {
                c = std::tolower(c);
            }
            if (s2.find(lo) != s2.end()) continue;
            s2[lo] = word;
            string star = lo;
            for (auto &c: star) 
                if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u') c='*';
            if (s3.find(star) == s3.end()) s3[star]=word;
        }
        vector<string>ans;
        for (auto q: queries) {
            if (s1.find(q)!=s1.end()) {
                ans.emplace_back(q);
                continue;
            }
            string lo = q;
            for (auto &c : lo) {
                c = std::tolower(c);
            }
            if (s2.find(lo)!=s2.end()) {
                ans.emplace_back(s2[lo]);
                continue;
            }
            string star = lo;
            for (auto &c: star) 
                if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u') c='*';
            if (s3.find(star)!=s3.end()) {
                ans.emplace_back(s3[star]);
                continue;
            }
            ans.emplace_back("");
        }
        return ans;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    return 0;
}