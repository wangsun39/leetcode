#include "lc_pub.h"


class Trie{
public:
    Trie*children[27];
    bool isEnd;
    Trie(){
       memset(children,0,sizeof(children));
       isEnd=false; 
    }
    void insert(string&s){
        Trie*root=this;
        for(char c:s){
            int idx=c-'a';
            if(c=='/')idx=26;
            if(root->children[idx]==nullptr)root->children[idx]=new Trie();
            root=root->children[idx];
        }
        root->isEnd=true;
    }
    bool startWith(string&s){
        // s的前缀在Trie树上
        Trie*root=this;
        int n=s.size();
        for(int i=0;i<n-1;i++){
            char c=s[i];
            int idx=c-'a';
            if(c=='/')idx=26;
            if(root->children[idx]==nullptr)return false;
            root=root->children[idx];
            if(root->isEnd==true&&s[i+1]=='/')return true;
        }
        return false;
    }
};


class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        Trie tr;
        vector<string> ans;
        ranges::sort(folder);
        for (auto &f: folder) {
            if (tr.startWith(f)) continue;
            tr.insert(f);
            ans.emplace_back(f);
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> arrays = parseGrid("[[1,2,3],[4,5],[1,2,3]]");
    Solution so;
    cout << so.nthUglyNumber(1000000000,2,217983653,336916467) <<endl;
    return 0;
}