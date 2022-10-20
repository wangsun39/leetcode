def calculate_res(nums, ops):
    try:
        r1 = my_op(nums[0], nums[1], ops[0])
        r2 = my_op(r1, nums[2], ops[1])
        r3 = my_op(r2, nums[3], ops[2])
    except ZeroDivisionError:
        return 0
    return r3


def my_op(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        try:
            return x // y
        except ZeroDivisionError:
            raise ZeroDivisionError
    elif op == '**':
        try:
            return int(x ** y)
        except ZeroDivisionError:
            raise ZeroDivisionError
    elif op == '&':
        return x & y
    elif op == '|':
        return x | y
    elif op == '^':
        return x ^ y
    elif op == '>>':
        return x >> y
    elif op == '<<':
        return x << y

# (2, 14, 29, 1024) ('*', '>>', '^')
# (1024, 32, 2, 1024) ('>>', '-', '&')
if __name__ == '__main__':
    nums = [1, 2,2,12,14,23,32,29,1024, 1024]  # 填拥有的数字卡
    ops = ["|", "^", "*", ">>", "&", "-"]  # 拥有的符号卡
    nums = [1,2,12,23,32,32,1024, 1024]  # 填拥有的数字卡
    ops = ["|", "&", "-", ">>"]  # 拥有的符号卡

    from itertools import permutations

    for n_perm in permutations(nums, 4):
        for o_perm in permutations(ops, 3):
            res = calculate_res(n_perm, o_perm)
            if res == 1024:
                print(n_perm, o_perm)

