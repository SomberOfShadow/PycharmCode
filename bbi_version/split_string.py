path = "/repo/gratci/workspace/executor/0/common-grat/GTOOLS/bin"
p = path.split("/")
print(len(p))
pa = ""
for i in range(0, len(p)-2):
    pa += p[i] + "/"
print(pa)
print(p[8])