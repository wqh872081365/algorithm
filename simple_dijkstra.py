#!/usr/bin/env python
# -*- coding:utf-8 -*-

# shortest_path
# Dijkstra算法

import sys
import heapq


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None


class Graph:
    def __init__(self):
        self.vert_dict = {}

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].adjacent[self.vert_dict[to]] = cost
        self.vert_dict[to].adjacent[self.vert_dict[frm]] = cost


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.id)
        shortest(v.previous, path)
    return


def dijkstra(aGraph, start, target):
    # Set the distance for the start node to zero
    start.distance = 0

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.distance, v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.visited = True

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.distance + current.adjacent[next]

            if new_dist < next.distance:
                next.distance = new_dist
                next.previous = current

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.distance, v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


def main():

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))

    print "all vertex shortest distance: "
    for v in g:
        path = [v.id]
        shortest(v, path)
        print v.id + ' ' +v.distance.__str__() + ' ' + str(path[::-1])


if __name__ == '__main__':
    main()
