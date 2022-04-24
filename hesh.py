#
a = [3, 2, 4, 1, 7]
k = 9
#
for t in a:
    if k > t:
        c = k - t
        for n in a:
           if n == c:
               print(f"Num {k} = {n} + {t}")
               exit()
               
               
