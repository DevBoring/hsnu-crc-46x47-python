class Node:
    def __init__(self):
        self.nexts = []  # 該節點是那些節點的輸入
        self.val = -1
        self.delay = 0
        self.gate = None
        self.ipt = []  # 那些節點是本節點的輸入


def t():
    pp, q, r, m = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]
    t = [int(i) for i in input().split()]
    nodes = []
    for i in range(pp + q + r):
        nodes.append(Node())
    for i in range(pp):
        nodes[i].val = p[i]
    for i in range(pp, pp + q):
        nodes[i].gate = t[i - pp]
    # print(nodes)

    for i in range(m):
        a, b = [int(i) for i in input().split()]
        a -= 1
        b -= 1
        nodes[a].nexts.append(b)

    p = [i for i in range(pp)]

    '''1 為 AND、2 為 OR、3 為 XOR、4 為 NO'''
    for i in p:
        if nodes[i].val == -1: continue
        for j in nodes[i].nexts:  # i節點是j節點的輸入
            nodes[j].ipt.append(i)  # j節點的輸入有添加i節點
            if nodes[j].gate == 4 and len(nodes[j].ipt) == 1:
                nodes[j].val = int(not nodes[nodes[j].ipt[0]].val)  # j節點的值，是j的輸入的值的相反
                nodes[j].delay = nodes[nodes[j].ipt[0]].delay + 1
                p.append(j)
            elif nodes[j].gate != 4 and len(nodes[j].ipt) == 2:
                p1, p2 = nodes[nodes[j].ipt[0]], nodes[nodes[j].ipt[1]]
                if nodes[j].gate == 1:
                    nodes[j].val = int(p1.val and p2.val)
                if nodes[j].gate == 2:
                    nodes[j].val = int(p1.val or p2.val)
                if nodes[j].gate == 3:
                    nodes[j].val = int(p1.val != p2.val)
                nodes[j].delay = max(p1.delay, p2.delay) + 1
                p.append(j)
    mm = 0
    for i in range(pp + q, pp + q + r):
        mm = max(nodes[nodes[i].ipt[0]].delay, mm)
    print(mm)
    for i in range(pp + q, pp + q + r):
        print(nodes[nodes[i].ipt[0]].val, end=' ')
    print()

if __name__ == "__main__":
    t()
