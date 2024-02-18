import sys
# from itertools import combinations
input = sys.stdin.readline

def prod(my_list):
    res = 1
    for l in my_list:
        res *= l
    return res

for _ in range(int(input())): # 1~100
    items_dict = dict()
    for a in range(int(input())): # 1~30
        name, kind = input().split()
        items_dict.setdefault(kind, 0)
        items_dict[kind] += 1
    items = list(items_dict.values())

    # total = 0
    # for i in range(1, len(items)+1):
    #     for com in list(combinations(items, i)):
    #         total += prod(com)
    # print(total)
    
    # 미친
    total = 1
    for i in items:
        total *= (i + 1)
    print(total-1)