from numpy import *
import operator
from KNN_demo import KNN
import math
# inx:分类向量
# dataSet:训练样本数据
# lables:向量标签
# k 距离最近的n个数目
def classify0(inx,dataSet,lable,k):
    ### 计算dataSet长度
    dataSize = dataSet.shape[0]
    ### 三维空间欧式距离公式  d = sqrt( (x1-x2)^2+(y1-y2)^2 )
    ### 将带入的分类向量 与存在的样本数据计算向量长度
    diffMat = tile(inx,(dataSize,1)) - dataSet  ###计算带入 x1-x2,y1-y2
    sqDiffMat = diffMat ** 2    ###计算带入 (x3)^2  ,   (y3)^2

    ###计算带入(x3)^2+(y3)^2 但是如果array只有一行，
    # 例如array([1, 2]), 则不能用sum(axis=1),只能用sum()
    sqDistances = sum(sqDiffMat,axis=1)

    print(sqDistances)
    distances = sqrt(sqDistances)  ###sqrt(x4,y4)
    print(distances)
    sortedDistIndex = argsort(distances)  ###从大到小排序 返回下标
    print(sortedDistIndex)

    classCount = {}   ###统计
    for i in range(k):
        classes = ''
        voteLable = lable[sortedDistIndex[i]]
        ### 选取的K个样本所属的类别个数进行统计
        classCount[voteLable] = classCount.get(voteLable,0)+1  #
        maxCount = 0
        ### 选取出现的类别次数最多的类别

    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
    return classes


group,lable = KNN.createDataSet()
print(group)
print(classify0([0,0],group,lable,3))
