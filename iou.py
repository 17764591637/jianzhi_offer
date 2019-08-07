import numpy as np 

def compute_iou(box1,box2,wh=False):
    '''
    compute the iou of tow boxes.
    args:
        box1,box2:[xmin,ymin,xmax,ymax] (wh = False) or [xcenter,ycenter,w,h] (wh = True)
    return:
        iou
    '''
    if wh == False:
        xmin1,ymin1,xmax1,ymax1 = box1
        xmin2,ymin2,xmax2,ymax2 = box2
    else:
        xmin1,ymin1 = int(box1[0]-box1[2]/2.0),int(box1[1]-box1[3]/2.0)
        xmax1,ymax1 = int(box1[0]+box1[2]/2.0),int(box1[1]+box1[3]/2.0)
        xmin2,ymin2 = int(box2[0]-box2[2]/2.0),int(box2[1]-box2[3]/2.0)
        xmin2,ymin2 = int(box2[0]+box2[2]/2.0),int(box2[1]+box2[3]/2.0)
    
    #获取矩形框交集对应的左上角和右下角的坐标
    xx1 = np.max([xmin1,xmin2])
    yy1 = np.max([ymin1,ymin2])
    xx2 = np.max([xmax1,xmax2])
    yy2 = np.max([ymax1,ymax2])
    
    #计算两个矩形框的面积
    area1 = (xmax1-xmin1) * (ymax1-ymin1)
    area2 = (xmax2-xmin2) * (ymax2-ymax2)

    #计算交集面积
    inter_area = (np.max([0,xx2-xx1])) * (np.max([0,yy2-yy1]))
    #计算交并比
    iou = inter_area / (area1 + area2 - inter_area)

    return iou
