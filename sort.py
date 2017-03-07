#!/usr/bin/env python
# -*- coding:utf-8 -*-


# quicksort

# Wikipedia
# 想去掉重复值只需把'='去掉即可
def quicksort(a):
    if len(a) <= 1:
        return a
    return quicksort([x for x in a[1:] if x <= a[0]]) + [a[0]] + quicksort([x for x in a[1:] if x > a[0]])








def main():
    print quicksort([12,4,5,6,7,3,6,1,15])


if __name__ == '__main__':
    main()
