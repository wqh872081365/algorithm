#!/usr/bin/env python
# -*- coding:utf-8 -*-


# quicksort

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    return quick_sort([x for x in lst[1:] if x < lst[0]]) + [lst[0]] + quick_sort([x for x in lst[1:] if x >= lst[0]])


def quick_sort_lomuto(lst, lo, hi):

    def partition(lst, lo, hi):
        p = lst[hi]
        i = lo
        for j in xrange(lo, hi):
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
    for i in xrange(1, len(lst)):
        tem = lst[i]
        j = i
        for j in xrange(i, 0, -1):
            if lst[j-1] > tem:
                lst[j] = lst[j-1]
            else:
                break
        else:
            j -= 1
        lst[j] = tem
    return lst


# 冒泡排序
def bubble_sort(lst):
    j = len(lst) - 1
    while j > 0:
        n_j = 0
        for i in xrange(0, j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                n_j = i
        j = n_j
    return lst


# 选择排序
def selection_sort(lst):
    n = len(lst)
    for i in xrange(n-1):
        min_i = i
        for j in xrange(i+1, n):
            if lst[min_i] > lst[j]:
                min_i = j
        if min_i != i:
            lst[min_i], lst[i] = lst[i], lst[min_i]
    return lst


# 堆排序　使用heapq模块
def heapsort(lst):

    from heapq import heapify, heappop

    heapify(lst)
    return [heappop(lst) for _ in xrange(len(lst))]


# 堆排序　
def heap_sort(lst):

    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child+1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    n = len(lst)

    # 创建最大堆
    for start in xrange(n//2-1, -1, -1):
        sift_down(start, n-1)

    # 堆排序
    for end in xrange(n-1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end-1)
    return lst


def merge_sort(lst, l, r):

    def merge(lst, l, m, r):
        left = lst[l: m+1]
        left.append(float('inf'))
        right = lst[m+1: r+1]
        right.append(float('inf'))
        i, j = 0, 0
        for k in xrange(l, r+1):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1

    if r > l:
        mid = (r + l) / 2
        merge_sort(lst, l, mid)
        merge_sort(lst, mid + 1, r)
        merge(lst, l, mid, r)


def main():
    lst = [12,4,5,6,7,3,6,1,15]
    # print quick_sort(lst)
    # quick_sort_lomuto(lst, 0, len(lst)-1)
    # quick_sort_hoare(lst, 0, len(lst)-1)
    # print insert_sort(lst)
    # print bubble_sort(lst)
    # print selection_sort(lst)
    # print heapsort(lst)
    # print heap_sort(lst)
    # merge_sort(lst, 0, len(lst)-1)
    # print lst


if __name__ == '__main__':
    main()
