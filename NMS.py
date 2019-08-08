'''
NMS实现步骤：
1.获取当前目标类别下所有box信息
2.按打分最高到最低将box排序，并记录当前分数最高的box
3.计算置信度最大的box与剩下所有的box的IOU，移除所有大于IOU阈值的box
4.对剩下的box，循环执行（2）和（3）直到所有的box均满足要求（即不能再移除box）
'''
import numpy as np 

boxes = np.array([[100,100,210,210,0.72],
[250,250,420,420,0.8],
[220,220,320,330,0.92],
[100,100,210,210,0.72],
[230,240,325,330,0.81],
[220,230,315,340,0.9]])

def py_cpu_nms(dets, thresh):
    #dets的数据格式是dets[[xmin,ymin,xmax,ymax,scores]....]
    x1 = dets[:,0]
    y1 = dets[:,1]
    x2 = dets[:,2]
    y2 = dets[:,3]
    areas = (y2-y1+1) * (x2-x1+1)
    scores = dets[:,4]
    
    #keep用于存放NMS后剩余的方框
    keep = []
    #取出分数从大到小排列的索引。.argsort()是从小到大排列，[::-1]是列表头和尾颠倒一下。
    index = scores.argsort()[::-1]
    #上面这两句比如分数[0.72 0.8  0.92 0.72 0.81 0.9 ]    
    # 对应的索引index[  2   5    4     1    3   0  ]记住是取出索引，scores列表没变。
    
    #index会剔除遍历过的方框，和合并过的方框。 
    while index.size > 0:

        #取出第一个方框进行和其他方框比对，看有没有可以合并的
        i = index[0]
        
        #因为我们这边分数已经按从大到小排列了。
        #所以如果有合并存在，也是保留分数最高的这个，也就是我们现在那个这个
        #keep保留的是索引值，不是具体的分数。     
        keep.append(i)
 
        #计算交集的左上角和右下角
        #这里要注意，比如x1[i]这个方框的左上角x和所有其他的方框的左上角x的
        x11 = np.maximum(x1[i], x1[index[1:]])   
        y11 = np.maximum(y1[i], y1[index[1:]])
        x22 = np.minimum(x2[i], x2[index[1:]])
        y22 = np.minimum(y2[i], y2[index[1:]])
        
        #这边要注意，如果两个方框相交，X22-X11和Y22-Y11是正的。
        #如果两个方框不相交，X22-X11和Y22-Y11是负的，我们把不相交的W和H设为0.
        w = np.maximum(0, x22-x11+1)    
        h = np.maximum(0, y22-y11+1)    
       
        #计算重叠面积就是上面说的交集面积。不相交因为W和H都是0，所以不相交面积为0
        overlaps = w*h

        #这个就是IOU公式（交并比）。
        #得出来的ious是一个列表，里面拥有当前方框和其他所有方框的IOU结果。
        ious = overlaps / (areas[i]+areas[index[1:]] - overlaps)
        
        #接下来是合并重叠度最大的方框，也就是合并ious中值大于thresh的方框
        #合并的操作就是把他们剔除，因为我们合并这些方框只保留下分数最高的。
        #这里np.where(ious<=thresh)[0]是一个固定写法。
        idx = np.where(ious<=thresh)[0]#小于等于阈值的留下
        #把留下来框再进行NMS操作
        #这边留下的框是去除当前操作的框，和当前操作的框重叠度大于thresh的框
        #每一次都会先去除当前操作框，所以索引的列表就会向前移动移位，要还原就+1，向后移动一位
        index = index[idx+1]


    return keep


res = py_cpu_nms(boxes,0.7)
print(boxes[res])


