#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 简单匹配
def naive_match(s, p):
    m = len(s)
    n = len(p)
    for i in range(m-n+1):
        if s[i: i+n] == p:
            return True
    return False

# 部分匹配表
def partial_table(p):
    prefix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[: i])
        postfix = {p[j: i + 1] for j in range(1, i + 1)}
        s_list = [len(s) for s in (prefix & postfix)]
        ret.append(max(s_list) if s_list else 0)
    return ret

# KMP
def kmp_match(s, p):
    m = len(s)
    n = len(p)
    cur = 0
    table = partial_table(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)
                break
        else:
            return True
    return False
