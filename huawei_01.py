class Solutuion:
    def sort(self,m,nums_list):
        nums_dict = {}
        for i in range(m):
            nums_dict.update(nums_list[i])
        dic1SortList = sorted(nums_dict.items(),key = lambda x:x[1],reverse=True)
        return dic1SortList

s = Solutuion()
res = s.sort(m=3,
nums_list=[
    {'d1':0.8,'d2':0.6,'d3':0.2},
    {'d4':0.9,'d5':0.6,'d6':0.3},
    {'d7':0.9,'d8':0.4,'d9':0.3}
])
print(res)
#[('d4', 0.9), ('d7', 0.9), ('d1', 0.8), ('d2', 0.6), ('d5', 0.6), ('d8', 0.4), ('d6', 0.3), ('d9', 0.3), ('d3', 0.2)]