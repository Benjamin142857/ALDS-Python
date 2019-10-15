"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : 10/4/2019
    Remark      : Test005_lklst性能测试
"""
from timeit import Timer
from ADT_List import SingleLinkList
LST_LEN = 10000
TEST_TIMES = 100
lst_4 = list(range(10000))
lklst_4 = SingleLinkList(*lst_4)


# 1. append尾插生成比较测试
def test_1a():
    ret = []
    for i in range(LST_LEN):
        ret.append(i)
    return ret

def test_1b():
    ret = SingleLinkList()
    for i in range(LST_LEN):
        ret.append(i)
    return ret

# 2. 头插入生成
def test_2a():
    ret = []
    for i in range(LST_LEN):
        ret.insert(0, i)
    return ret

def test_2b():
    ret = SingleLinkList()
    for i in range(LST_LEN):
        ret.add(i)
    return ret

# 3. insert插入生成
def test_3a():
    ret = [1, 2, 3, 4]
    for i in range(LST_LEN):
        ret.insert(2, i)
    return ret

def test_3b():
    ret = SingleLinkList(1, 2, 3, 4)
    for i in range(LST_LEN):
        ret.insert(2, i)
    return ret


# 4. 查询测试
def test_4a():
    for i in range(LST_LEN):
        temp = lst_4[i]


def test_4b():
    for i in range(LST_LEN):
        temp = lklst_4[i]


if __name__ == '__main__':
    timer1a = Timer("test_1a()", "from __main__ import test_1a")
    timer1b = Timer("test_1b()", "from __main__ import test_1b")
    print('[1a] list append 尾插测试：{:.6f} s'.format(timer1a.timeit(TEST_TIMES) / TEST_TIMES))
    print('[1a] 单链表 append 尾插测试：{:.6f} s'.format(timer1b.timeit(TEST_TIMES) / TEST_TIMES))
    print('\n')
    timer2a = Timer("test_2a()", "from __main__ import test_2a")
    timer2b = Timer("test_2b()", "from __main__ import test_2b")
    print('[2a] list insert头插测试：{:.6f} s'.format(timer2a.timeit(TEST_TIMES)/TEST_TIMES))
    print('[2a] 单链表 add头插测试：{:.6f} s'.format(timer2b.timeit(TEST_TIMES)/TEST_TIMES))
    print('\n')
    timer3a = Timer("test_3a()", "from __main__ import test_3a")
    timer3b = Timer("test_3b()", "from __main__ import test_3b")
    print('[3a] list insert i=2 插入测试：{:.6f} s'.format(timer3a.timeit(TEST_TIMES) / TEST_TIMES))
    print('[3b] 单链表 insert i=2 插入测试：{:.6f} s'.format(timer3b.timeit(TEST_TIMES) / TEST_TIMES))
    print('\n')
    timer4a = Timer("test_4a()", "from __main__ import test_4a")
    timer4b = Timer("test_4b()", "from __main__ import test_4b")
    print('[4a] list 索引查找测试：{:.6f} s'.format(timer4a.timeit(TEST_TIMES) / TEST_TIMES))
    print('[4b] 单链表 索引查找测试：{:.6f} s'.format(timer4b.timeit(TEST_TIMES) / TEST_TIMES))
    print('\n')