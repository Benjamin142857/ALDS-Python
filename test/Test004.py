"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : 9/29/2019
    Remark      : Test004
"""

if __name__ == '__main__':
    # 1. 用户数输入
    user_num = int(input())
    # 2. k列表输入
    k_lst = input().split(' ')
    k_lst = list(map(lambda x: int(x), k_lst))
    # 3. 查询组数输入
    qs_num = int(input())
    # 4. 查询 l, r, k输入
    qs_lst_lst = []
    for i in range(qs_num):
        temp_lst = input().split(' ')
        qs_lst_lst.append(list(map(lambda x: int(x), temp_lst)))

    # 输出初始化
    ret_lst = []

    for l, r, k in qs_lst_lst:
        res = len([temp_k for temp_k in k_lst[l - 1:r] if temp_k == k])
        ret_lst.append(res)

    for ret in ret_lst:
        print(ret)
