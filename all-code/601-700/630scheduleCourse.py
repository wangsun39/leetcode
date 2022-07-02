import heapq
class Solution:
    def scheduleCourse(self, courses):
        # 先按课程结束时间排序(可以反正：最优解都能表示为按结束时间递增的顺序上课的一个解)
        courses.sort(key=lambda l:l[1])
        curTime = 0
        selectCourses = []
        for pair in courses:
            # 依次将排序的课程放入选择的课程中，
            # 如果发现不能选这门课，则比较已选的课程中时间最长的课是否比当前课程时间长：
            #     如果是，则将之前时间最长的课取消，选择当前课程，因为这样可以在更短的时间内完成相同数量的课程
            #     如果不是，则不选当前的课程，因为如果选择当前课程，课程总数量不会增加，课程总时间却长了
            if curTime + pair[0] <= pair[1]:
                curTime += pair[0]
                heapq.heappush(selectCourses, -pair[0]) #取相反数构造大顶推
            elif selectCourses and -selectCourses[0] > pair[0]:
                curTime += (selectCourses[0] + pair[0])
                heapq.heappop(selectCourses)
                heapq.heappush(selectCourses, -pair[0])
        return len(selectCourses)
