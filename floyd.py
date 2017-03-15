#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys


def floydWarshall(dist):

    n = len(dist)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for i in range(n):
        for j in range(n):
            if (dist[i][j] == sys.maxint):
                print "%5s" % ("INF"),
            else:
                print "%5d\t" % (dist[i][j]),
            if j == n - 1:
                print "\n"


def main():

    g = [[0, 5, sys.maxint, 10],
         [5, 0, 3, sys.maxint],
         [sys.maxint, 3, 0, 1],
         [10, sys.maxint, 1, 0]
         ]

    floydWarshall(g)


if __name__ == '__main__':
    main()

