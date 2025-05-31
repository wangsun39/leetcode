#include "lc_pub.h"

using namespace std;

class Solution {
    public:
    int snakesAndLadders(vector<vector<int>>& board) {
        reverse(board.begin(), board.end());
        int r = board.size(), c = board[0].size();
        for (int i=1;i<r;i+=2) {
            reverse(board[i].begin(), board[i].end());
        }
        vector<int> lines;
        for (auto &row: board) {
            for (int x: row)
                if (x != -1) lines.emplace_back(x - 1);
                else lines.emplace_back(-1);
        }
        vector<int>vis(r * c, 0);
        deque<int> dq1;
        dq1.push_back(0);
        vis[0] = 1;
        int ans = 1;
        while (dq1.size()) {
            deque<int> dq2;
            while (dq1.size()) {
                int x = dq1[0];
                dq1.pop_front();
                for (int i= 1;i<7;i++) {
                    int y = x + i;
                    if (y == r * c - 1) return ans;
                    if (vis[y]==1) continue;
                    vis[y]=1;
                    if (lines[y] == -1) {
                        dq2.push_back(y);
                        continue;
                    }
                    int z=lines[y];
                    if (z==r*c-1) return ans;
                    if (vis[z]==2) continue;
                    dq2.push_back(z);
                    vis[z]=2;
                }
            }
            dq1=move(dq2);
            ans++;
        }
        return -1;
    }
    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>> arrays = parseGrid("[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]");
    Solution so;
    cout << so.snakesAndLadders(arrays) <<endl;
    return 0;
}