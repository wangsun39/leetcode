class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i) for i in range(1, n+1)]
        for i in range(3, n+1, 3):
            res[i - 1] = 'Fizz'
        for i in range(5, n+1, 5):
            res[i - 1] = 'Buzz'
        for i in range(15, n+1, 15):
            res[i - 1] = 'FizzBuzz'
        return res

