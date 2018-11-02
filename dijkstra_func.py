import collections
import copy


def dijkstra(d_l, n, f):
    g = collections.defaultdict(list)
    for u, v, w in d_l:
        g[u].append([v, w])
    d = {i: float("inf") for i in n}
    d[f] = 0
    s = set([])
    q = copy.deepcopy(n)
    p = {}
    while q:
        u_d, u = min([[d[k], k] for k in q])
        if u_d != float("inf"):
            q.remove(u)
            s.add(u)
            for v, w in g[u]:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    p[v] = u
        else:
            break
    return d, p


def get_path(i, p, p_l):
    if i in p_l:
        return p_l.get(i)
    else:
        path = [i]
        if i in p:
            path.extend(get_path(p[i], p, p_l))
        p_l[i] = path
        return p_l[i]


def main():
    d_l = [["a", "b", 7], ["b", "a", 7], ["a", "c", 9], ["c", "a", 9], ["a", "f", 14], ["f", "a", 14], ["b", "c", 10],
           ["c", "b", 10], ["b", "d", 15], ["d", "b", 15], ["c", "d", 11], ["d", "c", 11], ["c", "f", 2], ["f", "c", 2],
           ["d", "e", 6], ["e", "d", 6], ["e", "f", 9], ["f", "e", 9]]
    n = {"a", "b", "c", "d", "e", "f"}
    f = "a"
    d, p = dijkstra(d_l, n, f)
    p_l = {}
    for i in n:
        print("to:%s, dist:%s, path:%s" % (i, d[i], get_path(i, p, p_l)[::-1]))


if __name__ == '__main__':
    main()
