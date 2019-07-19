zhishu_list = {2,7}
start = 14
res= []
for j in zhishu_list:
    if j not in {2,3,5}:
        start += 1
else:
    res.append(14)
    start += 1
    
print(res)