'''
给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。
如给定序列[6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:

[6] = 6 * 6 = 36;
[2] = 2 * 2 = 4;
[1] = 1 * 1 = 1;
[6,2] = 2 * 8 = 16;
[2,1] = 1 * 3 = 3;
[6, 2, 1] = 1 * 9 = 9;
从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。
区间内的所有数字都在[0, 100]的范围内;
输入描述:
第一行输入数组序列长度n，第二行输入数组序列。

输出描述:
输出数组经过计算后的最大值。
输入例子1:
3
6 2 1
输出例子1:
36
'''
n=int(raw_input())
arr=[int(x) for x in raw_input()[:-1].split(' ')]
 
arr.append(-1)
i=0
stack_pop_before=[]
stack=[]
ans=0
while i<=n:
    num=arr[i]
    pop_sum=0
    pop_before=0
    while stack and num<stack[-1]:
        pop_num=stack.pop()
        pop_sum+=pop_num
        pop_before+=stack_pop_before.pop()
        ans=max(ans,(pop_before+pop_sum)*pop_num)
    stack_pop_before.append(pop_before+pop_sum)
    stack.append(num)
    i+=1
print ans