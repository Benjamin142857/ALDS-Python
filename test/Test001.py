"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : 9/23/2019
    Remark      : Test001 - abc试探
"""
import time

# a + b + c = 1000
# a^2 + b^2 = c^2
# 求自然数 a, b, c 的所有组合

if __name__ == '__main__':
    s_time = time.time()
    ret_lst = []
    abc_sum = 1000
    for a in range(0, abc_sum+1):
        for b in range(0, abc_sum+1):
            c = abc_sum - a - b
            if (a**2 + b**2) == c**2:
                ret_lst.append({
                    'a': a,
                    'b': b,
                    'c': c,
                })
    use_time = time.time()-s_time
    print('用时:{:.4f} s'.format(use_time))
    for comb in ret_lst:
        print(comb)

