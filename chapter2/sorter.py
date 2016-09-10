import sys

lines=sys.stdin.readlines()
content=[]
for i in lines:
    i=i[:-1]
    content.append(i)
for n in content:
    if n == "":
        content.remove(n)
    else:
        continue
for m in content:
    if m == "":
        content.remove(m)
    else:
        continue
for k in content:
    if k == "":
        content.remove(k)
    else:
        continue
print(content.sort())

# for line in content:
#     print(line)
print(content)
