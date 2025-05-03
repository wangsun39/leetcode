#include "lc_pub.h"

class Solution {
    public:
        long long countOfSubstrings(string word, int k) {
            vector<int> idx;
            int n = word.size();
            unordered_map<int,int> counter;
            vector<int> next_con(n, n);  // 下个辅音的位置
            for (int i=n-2;i>=0;i--) {
                if (word[i+1]=='a'||word[i+1]=='e'||word[i+1]=='i'||word[i+1]=='o'||word[i+1]=='u')
                    next_con[i] = next_con[i+1];
                else next_con[i] = i+1;
            }
            auto check = [&]() -> int {
                int cntv=0,cntc=0;
                for (auto &it: counter) {
                    if (it.second) {
                        if (it.first == 0) cntc+=it.second;
                        else cntv++;
                    }
                }
                if (cntc>k) return 1;  // 辅音多了
                if (cntv<5||cntc<k) return -1;  // 字母不够
                return 0;  // 满足要求
            };

            int r=0,ans=0;   // 窗口  [l,r)
            for (int l=0;l<n;l++) {
                if (l>0) {
                    if (word[l-1]=='a'||word[l-1]=='e'||word[l-1]=='i'||word[l-1]=='o'||word[l-1]=='u') counter[word[l-1]]--;
                    else counter[0]--;
                    // continue;
                }
                while (check()<0 && r < n) {
                    if (word[r]=='a'||word[r]=='e'||word[r]=='i'||word[r]=='o'||word[r]=='u') counter[word[r]]++;
                    else counter[0]++;
                    r++;
                }
                int ch = check();
                if (ch==1) continue;
                if (ch==0) {
                    ans += (next_con[r-1]-r+1);
                    continue;
                }
                break;
            }
            return ans;
        }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    Solution so;
    auto v = so.countOfSubstrings("aeioeu",1);
    // auto v = so.countOfSubstrings("aeiou",0);
    cout << v << endl;
    return 0;
}
