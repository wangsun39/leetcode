#include "lc_pub.h"

class Solution {
    static constexpr int DIRS[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public:
        bool exist(vector<vector<char>>& board, string word) {
            int m = board.size(), n = board[0].size();
            auto dfs = [&](this auto&& dfs, int i, int j, int k) -> bool {  // this auto&& 是g++ 在C++23中支持的，允许lambda中递归
                if (board[i][j] != word[k]) { // 匹配失败
                    return false;
                }
                if (k + 1 == word.length()) { // 匹配成功！
                    return true;
                }
                board[i][j] = 0; // 标记访问过
                for (auto& [dx, dy] : DIRS) {
                    int x = i + dx, y = j + dy; // 相邻格子
                    if (0 <= x && x < m && 0 <= y && y < n && dfs(x, y, k + 1)) {
                        return true; // 搜到了！
                    }
                }
                board[i][j] = word[k]; // 恢复现场
                return false; // 没搜到
            };
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (dfs(i, j, 0)) {
                        return true; // 搜到了！
                    }
                }
            }
            return false; // 没搜到
        }

    };

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    std::vector<std::vector<char>> board = {
        {'A', 'B', 'C', 'E'},
        {'S', 'F', 'C', 'S'},
        {'A', 'D', 'E', 'E'}
    };
    Solution so;
    auto v = so.exist(board, "ABCCED");
    cout << v << endl;
    return 0;
}
