class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def compareVersion(self, version1: str, version2: str):
        def isHave1_9(str):
            for i in str:
                if i >= '1' and i <= '9':
                    return True
            return False
        pos1_begin, pos2_begin = 0, 0
        while True:
            len1 = version1[pos1_begin:].find('.')
            len2 = version2[pos2_begin:].find('.')
            cur_ver1 = int(version1[pos1_begin:pos1_begin+len1]) if len1 != -1 else int(version1[pos1_begin:])
            cur_ver2 = int(version2[pos2_begin:pos2_begin+len2]) if len2 != -1 else int(version2[pos2_begin:])
            if cur_ver1 > cur_ver2:
                return 1
            elif cur_ver1 < cur_ver2:
                return -1
            elif len1 == -1 and len2 == -1:
                return 0
            elif len1 == -1:
                if isHave1_9(version2[pos2_begin + len2 + 1:]):
                    return -1
                else:
                    return 0
            elif len2 == -1:
                if isHave1_9(version1[pos1_begin + len1 + 1:]):
                    return 1
                else:
                    return 0
            pos1_begin = pos1_begin + len1 + 1
            pos2_begin = pos2_begin + len2 + 1
        return 0

so = Solution()
#print(so.compareVersion('1.1.2', '1.1.1'))
#print(so.compareVersion("7.5.2.4", "7.5.3"))
print(so.compareVersion("7.5.3.4", "7.5.3"))
print(so.compareVersion("1.0", "1"))
