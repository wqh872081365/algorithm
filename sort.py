#!/usr/bin/env python
# -*- coding:utf-8 -*-


# quicksort

# Wikipedia
# 想去掉重复值只需把'='去掉即可
def quicksort(a):
    if len(a) <= 1:
        return a
    return quicksort([x for x in a[1:] if x <= a[0]]) + [a[0]] + quicksort([x for x in a[1:] if x > a[0]])


# 插入排序
def insert_sort(lst):
    n=len(lst)
    if n==1:
        return lst
    for i in range(1,n):
        for j in range(i,0,-1):
            if lst[j]<lst[j-1]: lst[j],lst[j-1]=lst[j-1],lst[j]
    return lst






def main():
    lst = [12,4,5,6,7,3,6,1,15]
    # print quicksort(lst)
    print insert_sort(lst)


if __name__ == '__main__':
    main()
