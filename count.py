from collections import Counter

with open("p1.txt", "r") as f:
    file = f.read()
    sps = file.split()

    count = []
    cn = []
    for sp in sps:
        if sp in count:
            indexs = count.index(sp)
            cn[indexs] += 1
        else:
            count.append(sp)
            cn.append(1)

print(count)
print(cn)
