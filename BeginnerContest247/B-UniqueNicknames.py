import sys

n = int(input())
lines = sys.stdin.readlines()

name_dict = {}
nicknames = []
flag = 'Yes'
cnt = 0
for line in lines:
    s, t = line.split()
    if s in name_dict.keys():
        if t in name_dict[s]:
            flag = 'No'
        name_dict[s].append(t)
    else:
        name_dict.update({s: [t]})
    nicknames.append(t)

    if 0 >= len(s) and len(s) > 10:
        flag = 'No' 
    if 0 >= len(t) and len(t) > 10:
        flag = 'No' 
nicknames = set(nicknames)

for s, t_list in name_dict.items():
    if flag == 'No':
        break

    if len(t_list) == 1:
        if s in nicknames and t_list[0] in name_dict.keys():
            flag = 'No'
    else:
        for t in t_list:
            if flag == 'No':
                break
            if t in name_dict.keys():
                flag = 'No'
                break
            for key, val in name_dict.items():
                if s == key:
                    continue
                if t in val:
                    flag = 'No'
                    break

print(flag)
