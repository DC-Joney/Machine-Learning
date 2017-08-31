# coding=utf-8
# -*- coding: utf-8 -*-
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import *
from KNN_demo import KNNFile
import platform


# 判断系统是windwos系统 还是linux系统
#指定默认字体
if(platform.system() == "Linux"):
    font = FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-microhei.ttc')
    # matplotlib.rcParams['font.sans-serif'] = ['AR PL UMing TW MBE']
    # matplotlib.rcParams['font.family'] = 'sans-serif'
    print("Linux系统字体")
else:
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'


#coding:utf-8
from numpy import  *
import operator
import matplotlib
import matplotlib.pyplot as plt
from KNN_demo import KNNFile

#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False


# returnMat,datingLabels = KNNFile.file2matrix("D:\datingTestSet.txt")


# print(returnMat[:10])
# print(15.0*array(datingLabels))
# print(datingLabels[:,1])
## 归一化数据,保证特征等权重

def matplotKNN(returnMat,datingLabels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    type1 = ax.scatter(returnMat[:, 0], returnMat[:, 1], 15 * array(datingLabels), 15 * array(datingLabels))
    # x1 = array([[1,2,3,4,5],[5,4,3,2,1],[6,7,8,9,10],[11,12,13,14,15]])
    # y2 = array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,6],[1,2,3,4,5]])
    # lables = [2,3,4,5]
    # print(x1[:,1])
    # type1 = ax.scatter(x1[:,1],y2[:,2],10*array(lables),10*array(lables))
    plt.xlabel('玩视频游戏所消耗的时间百本比',fontproperties=font)
    plt.ylabel('每年获取的飞行长客里程数',fontproperties=font)
    plt.legend([type1],['1'],loc='upper right')
    plt.show()

## 归一化数据,保证特征等权重
# 矩阵中的三维数据 权重一致 所以 不会影响到其他计算
def autoNorm(dataSet):
    minVals = dataSet.min(0)  # 获取训练样本中最小的数据
    print(minVals)
    maxVals = dataSet.max(0)  # 获取训练样本中最大的数据
    print(maxVals)
    ranges = maxVals - minVals  # 获取区间范围
    plt.xlabel('玩视频游戏所消耗的时间百本比')
    plt.ylabel('每年获取的飞行长客里程数')
    plt.legend(loc='upper right')
    plt.show()

# 矩阵中的三维数据 权重一致 所以 不会影响到其他计算
def autoNorm(dataSet):
    minVals = dataSet.min(0)  #获取训练样本中最小的数据
    print(minVals)
    maxVals = dataSet.max(0)  #获取训练样本中最大的数据
    print(maxVals)
    ranges = maxVals - minVals  #获取区间范围

    print(ranges)
    normDataSet = zeros(shape(dataSet))  ##建立与dataSet结构一样的矩阵
    # print(normDataSet)
    m = dataSet.shape[0]
    print(dataSet.shape[1])
    print(dataSet)
    normDataSet = dataSet - tile(minVals, (m, 1))
    print(normDataSet)
    normDataSet /= tile(ranges, (m, 1))
    print(normDataSet)
    return normDataSet, ranges, minVals



# KNN算法
def classify0(inx,dataSet,lable,k):
    dataSize = dataSet.shape[0]
    diff = tile(inx,(dataSet,1))-dataSet
    sqdiff = diff ** 2
    squareDist =sum(sqdiff,axis=1)
    dist = squareDist ** 0.5 #开平方根

    sortedDistIndex = argsort(dist) #从距离最小到距离最大

    classCount = {}
    for i in range(k):
        #取出对应类型
        voteLale = lable[sortedDistIndex[i]]
        classCount[voteLale] = classCount.get(voteLale,0)+1
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key

    return  classes


#测试(选取10%测试)

def datingTest(fileName):
    rate = 0.10
    datingDataMat,datingLables = KNNFile.file2matrix(fileName)
    norMat,ranges,minVals = autoNorm(datingDataMat)
    #获取训练样本的矩阵长度
    m = norMat.shape[0]
    #获取训练样本的测试长度
    testNum = int(m * rate)
    errorCount = 0.0
# returnMat,classModel = KNNFile.file2matrix("datingTestSet.txt")
#
# # matplotKNN(returnMat,classModel)
# autoNorm(returnMat)

    normDataSet = dataSet - tile(minVals,(m,1))
    print(normDataSet)
    normDataSet /= tile(ranges, (m, 1))
    print(normDataSet)
    return normDataSet,ranges,minVals

