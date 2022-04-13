import sys

n = int(input())
lines = sys.stdin.readlines()

name_dict = {}
nicknames = []
flag = 'Yes'
for line in lines:
    s, t = line.split()
    if s in name_dict.keys():
        name_dict[s] +=1
    else:
        name_dict.update({s: 0})
    if t in name_dict.keys():
        name_dict[t] +=1
    else:
        name_dict.update({t: 0})
    nicknames.append((s, t))

for s, t in nicknames:
    if name_dict[s] > 0 and name_dict[t] > 0:
        flag = 'No'
        break

print(flag)