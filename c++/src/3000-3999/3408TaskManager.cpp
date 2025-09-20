#include "lc_pub.h"

struct Compare {
    bool operator()(const std::vector<int>& a, const std::vector<int>& b) {
        if (a[0] == b[0]) return true;
            return a[1] < b[1]; // 最大堆（按第二个元素）
        return a[0] > b[0];
    }
};

class TaskManager {
public:
    TaskManager(vector<vector<int>>& tasks) {
        for (auto &t: tasks) {
            add(t[0], t[1], t[2]);
        }
    }
    
    void add(int userId, int taskId, int priority) {
        pq.push({priority, taskId, userId});
        task_priority[taskId] = priority;
        task_userId[taskId] = userId;
    }
    
    void edit(int taskId, int newPriority) {
        task_priority[taskId] = newPriority;
        pq.push({newPriority, taskId, task_userId[taskId]});
    }
    
    void rmv(int taskId) {
        task_priority.erase(taskId);
        task_userId.erase(taskId);
    }
    
    int execTop() {
        while (pq.size()) {
            auto t = pq.top();
            if (task_priority.find(t[1])==task_priority.end()||task_priority[t[1]]!=t[0]) {
                pq.pop();
                continue;
            }
            if (task_priority[t[1]]!=t[0]) {
                pq.pop();
                t[0] = task_priority[t[1]];
                pq.push(t);
                continue;
            }
            pq.pop();
            task_priority.erase(t[1]);
            task_userId.erase(t[1]);
            return t[2];
        }
        return -1;
    }

private:
    // priority_queue<vector<int>, vector<vector<int>>, Compare> pq;
    priority_queue<vector<int>> pq;
    unordered_map<int, int>task_priority;
    unordered_map<int, int>task_userId;
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto nums = parseGrid("[[8,21,43]]");

    TaskManager so(nums);
    so.rmv(21);
    so.add(6,15,38);
    so.rmv(15);
    so.add(3,15,23);
    cout << so.execTop() << endl;
    return 0;
}
