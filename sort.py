#!/usr/bin/env python
# -*- coding:utf-8 -*-


# quicksort

# Wikipedia

# 想去掉重复值只需把'='去掉即可
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    return quick_sort([x for x in lst[1:] if x <= lst[0]]) + [lst[0]] + quick_sort([x for x in lst[1:] if x > lst[0]])


def quick_sort_lomuto(lst, lo, hi):

    def partition(lst, lo, hi):
        p = lst[hi]
        i = lo
        for j in range(lo, hi):
            if lst[j] < p:
                if i != j:
                    lst[i], lst[j] = lst[j], lst[i]
                i += 1
        lst[i], lst[hi] = p, lst[i]
        return i

    if lo < hi:
        p = partition(lst, lo, hi)
        quick_sort_lomuto(lst, lo, p - 1)
        quick_sort_lomuto(lst, p + 1, hi)


def quick_sort_hoare(lst, lo, hi):

    def partition(lst, lo, hi):
        p = lst[lo]
        i = lo - 1
        j = hi + 1
        while True:
            while True:
                i += 1
                if lst[i] >= p:
                    break
            while True:
                j -= 1
                if lst[j] <= p:
                    break
            if i >= j:
                return j
            lst[i], lst[j] = lst[j], lst[i]

    if lo < hi:
        p = partition(lst, lo, hi)
        quick_sort_hoare(lst, lo, p)
        quick_sort_hoare(lst, p + 1, hi)


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
    if len(lst) <= 1:
        return lst
    for j in range(len(lst)-1,0,-1):
        for i in range(0, j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


# 选择排序
def selection_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lst[min_index] > lst[j]:
                min_index = j
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst


# 堆排序　使用heapq模块
from heapq import *


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h,value)
    return [heappop(h) for i in range(len(h))]


# 堆排序　
def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in xrange((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    for end in xrange(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst


def main():
    lst = [12,4,5,6,7,3,6,1,15]
    # print quick_sort(lst)
    # quick_sort_lomuto(lst, 0, len(lst)-1)
    # quick_sort_hoare(lst, 0, len(lst)-1)
    # print insert_sort(lst)
    # print bubble_sort(lst)
    # print selection_sort(lst)
    # print heapsort(lst)
    print heap_sort(lst)


if __name__ == '__main__':
    main()
