
# 可以参考 LCP04

def hungarian(graph):
    """
    匈牙利算法实现二分图最大匹配
    :param graph: 二分图的邻接矩阵表示，graph[u][v] 表示从左集合的 u 到右集合的 v 是否有边
    :return: 最大匹配的边数
    """
    num_left = len(graph)  # 左集合的顶点数
    num_right = len(graph[0])  # 右集合的顶点数
    match = [-1] * num_right  # 记录右集合中每个顶点匹配的左集合顶点， 也可以用set记录一对点
    # visited = [False] * num_right  # 记录右集合中每个顶点是否在当前增广路径中被访问过

    def dfs(u):
        for v in range(num_right):
            if graph[u][v] and not visited[v]:  # 如果有边且未访问过
                visited[v] = True
                if match[v] == -1 or dfs(match[v]):  # 如果 v 未匹配，或者 v 的匹配顶点可以找到新的匹配，这就保证的增广路径的结束
                    match[v] = u  # 更新匹配
                    return True
        return False

    max_match = 0
    for u in range(num_left):
        # 只能遍历二分图的一个分部
        # 每轮循环找一条新的增广路径
        # 每个 u 都能保证是之前没有匹配过的，这就保证了增广路径的开始
        visited = [False] * num_right  # 每次尝试匹配时重置访问标记
        if dfs(u):
            max_match += 1

    return max_match, match


# 示例
if __name__ == "__main__":
    # 二分图的邻接矩阵表示
    graph = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0]
    ]

    max_match, match = hungarian(graph)
    print("最大匹配数:", max_match)
    print("匹配关系（右集合顶点 -> 左集合顶点）:", match)
