
class Solution:
    def removeSubfolders1(self, folders):
        res = []
        for folder in folders:
            len1 = len(folder)
            need_add_folder = True
            i = len(res)
            for one in reversed(res):
                i -= 1
                len2 = len(one)
                if folder == one:
                    need_add_folder = False
                    continue
                if len1 < len2:
                    if folder == one[:len1] and '/' == one[len1]:
                        del(res[i])
                else:
                    if folder[:len2] == one and '/' == folder[len2]:
                        need_add_folder = False
                        continue
            if need_add_folder:
                res.append(folder)
        return res
    def removeSubfolders(self, folders):
        if len(folders) <= 1:
            return folders
        folders.sort()
        res = [folders[0]]
        for folder in folders[1:]:
            len1, len2 = len(res[-1]), len(folder)
            if res[-1] == folder:
                continue
            if len1 >= len2:
                pass
            if folder[:len1] == res[-1] and '/' == folder[len1]:
                continue
            res.append(folder)
        return res



obj = Solution()
print(obj.removeSubfolders(["/aa/ab/ac/ae","/aa/ab/af/ag","/ap/aq/ar/as","/ap/aq/ar","/ap/ax/ay/az","/ap","/ap/aq/ar/at","/aa/ab/af/ah","/aa/ai/aj/ak","/aa/ai/am/ao"]))
print(obj.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(obj.removeSubfolders( ["/a","/a/b/c","/a/b/d"]))
print(obj.removeSubfolders( ["/a/b/c","/a/b/d","/a/b/ca"]))

