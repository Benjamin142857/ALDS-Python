"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : 9/27/2019
    Remark      : Test002_timeit性能测试 - 对各种列表生成
"""
from timeit import Timer

LST_LEN = 10000
TEST_TIMES = 1000

# 1. append尾插生成
def test1():
    ret = []
    for i in range(LST_LEN):
        ret.append(i)
    return ret


# 2. insert插入生成
def test2():
    ret = []
    for i in range(LST_LEN):
        ret.insert(i, i)
    return ret


# 3. 列表生成式
def test3():
    ret = [i for i in range(LST_LEN)]
    return ret


# 4. 列表拼接: 与extend的区别在于，列表拼接是先生成 第三列表，然后把两个列表的元素放入第三列表
def test4():
    ret = []
    for i in range(LST_LEN):
        ret += [i]
    return ret


# 5. range迭代器list转化
def test5():
    ret = list(range(LST_LEN))
    return ret


# 6. list.extend: 相当于批量append
def test6():
    ret = []
    for i in range(LST_LEN):
        ret.extend([i])


# 7. insert头插入生成
def test7():
    ret = []
    for i in range(LST_LEN):
        ret.insert(0, i)
    return ret

if __name__ == '__main__':
    timer1 = Timer("test1()", "from __main__ import test1")
    timer2 = Timer("test2()", "from __main__ import test2")
    timer3 = Timer("test3()", "from __main__ import test3")
    timer4 = Timer("test4()", "from __main__ import test4")
    timer5 = Timer("test5()", "from __main__ import test5")
    timer6 = Timer("test6()", "from __main__ import test6")
    timer7 = Timer("test7()", "from __main__ import test7")
    print('[1. list.append] {}'.format(timer1.timeit(TEST_TIMES)))
    print('[2. list insert-1] {}'.format(timer2.timeit(TEST_TIMES)))
    print('[7. list insert0] {}'.format(timer7.timeit(TEST_TIMES)))
    print('[6. list expend] {}'.format(timer6.timeit(TEST_TIMES)))
    print('[3. 列表生成式    ] {}'.format(timer3.timeit(TEST_TIMES)))
    print('[4. 列表拼接      ] {}'.format(timer4.timeit(TEST_TIMES)))
    print('[5. list(range)  ] {}'.format(timer5.timeit(TEST_TIMES)))
