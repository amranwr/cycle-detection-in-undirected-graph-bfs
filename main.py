def go():
    adj = {
        1: [2,3,4],
        2: [1, 5, 6],
        3: [1],
        4: [1,7, 8],
        5: [2, 9,10],
        6: [2],
        7: [4,11,12],
        8: [4],
        9: [5],
        10:[5],
        11:[7],
        12:[7]
    }
    level = {1: 0}
    parent = {1: None}
    frontier = [1]
    f = 1
    cycle =False
    while frontier:
        print(frontier)
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = f
                    parent[v] = u
                    next.append(v)
                else:
                    if level[v] >= level[u]:
                        cycle = True
                        break
        if cycle:
            break
        frontier = next
        f += 1
    print("there is a cycle: {}".format(cycle))

if __name__ == '__main__':
    go()
