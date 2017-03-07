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
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1]=lst[j-1], lst[j]
    return lst


# 冒泡排序
def bubble_sort(lst):
    for j in range(len(lst)-1,0,-1):
        for i in range(0, j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


# 选择排序
def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lst[min_index] > lst[j]:
                min_index = j
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst



def main():
    lst = [12,4,5,6,7,3,6,1,15]
    # print quicksort(lst)
    # print insert_sort(lst)
    # print bubble_sort(lst)
    print selection_sort(lst)


if __name__ == '__main__':
    main()
