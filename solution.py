s = input()
length = len(s)
mid = int(length/ 2 - 0.5)
ls = list(s)
rev = ls[mid:]
rev.extend(ls[:mid])
sp = ' '
for i in range(length):
    print(sp*(length-i-1)+"".join(rev[:i+1]))
