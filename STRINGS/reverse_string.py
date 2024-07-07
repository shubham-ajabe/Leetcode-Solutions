s = input()
s = s.strip()
l = s.split()
i = len(l) - 1
l1 = list()
for x in l:
    l1.append(l[i])
    i = i - 1
ddx = ' '.join(l1)



# 151. Reverse Words in a String
