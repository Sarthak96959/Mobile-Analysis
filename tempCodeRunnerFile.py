import numpy as np 
var = {}
n = int(input())
for _ in range(n):
    
    lt = []
    for i in range(n):
        ele = list(map(int,input().split()))
        lt.append(ele)
    lt = np.array(lt)
    var[f"a{_}"] = lt

for i in var.keys():
    print(var[i])