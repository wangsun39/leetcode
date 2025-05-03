#include "lc_pub.h"

class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        vector<int> ans;
        int row = grid.size(), col = grid[0].size();
        for (int j = 0; j < col; j++) {
            int x = 0, y = j;
            while (true) {
                if (grid[x][y] == 1) {
                    if (y + 1 == col || grid[x][y + 1] == -1) {
                        ans.emplace_back(-1);
                        break;
                    }
                    y++;
                }
                else {
                    if (y == 0 || grid[x][y - 1] == 1) {
                        ans.emplace_back(-1);
                        break;
                    }
                    y--;
                }
                x++;
                if (x == row) {
                    ans.emplace_back(y);
                    break;
                }
            }
        }
        return ans;
    }

};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    // vector<vector<int>> grid = {{1,1,1,-1,-1},{1,1,1,-1,-1},{-1,-1,-1,1,1},{1,1,1,1,-1},{-1,-1,-1,-1,-1}};
    vector<vector<int>> grid = parseGrid("[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]");
    cout << grid.size() << "  " << grid[0].size()<< endl;

    Solution so;
    auto v = so.findBall(grid);
    cout << v << endl;
    return 0;
}
