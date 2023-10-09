class Solution:
    def diffWaysToCompute(self, input):
        input.replace(' ', '')
        set_result = self.compute(input)
        return set_result

    def add_list(self, l1, l2):
        l3 = []
        for i in l1:
            for j in l2:
                l3.append(i + j)
        return l3

    def sub_list(self, l1, l2):
        l3 = []
        for i in l1:
            for j in l2:
                l3.append(i -j)
        return l3

    def product_list(self, l1, l2):
        l3 = []
        for i in l1:
            for j in l2:
                l3.append(i * j)
        return l3

    def compute(self, input):
        if input.isdigit():
            return [int(input)]
        result = []
        for pos in range(len(input)):
            if '+' == input[pos]:
                result += self.add_list(self.compute(input[:pos]), self.compute(input[pos+1:]))
            elif '-' == input[pos]:
                result += self.sub_list(self.compute(input[:pos]), self.compute(input[pos+1:]))
            elif '*' == input[pos]:
                result += self.product_list(self.compute(input[:pos]), self.compute(input[pos+1:]))
        return result




so = Solution()
#print(so.findKthLargest([3,2,1,5,6,4], 2))
#print(so.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
#print(so.findKthLargest([7,6,5,4,3,2,1], 5))
print(so.diffWaysToCompute("2-1-1"))
print(so.diffWaysToCompute("2*3-4*5"))

