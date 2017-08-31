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


returnMat,datingLabels = KNNFile.file2matrix("D:\datingTestSet.txt")
print(returnMat)
# print(returnMat[:10])
# print(15.0*array(datingLabels))
# print(datingLabels[:,1])
fig = plt.figure()
ax = fig.add_subplot(111)
type1 = ax.scatter(returnMat[:,0],returnMat[:,1],15*array(datingLabels),15*array(datingLabels))
# x1 = array([[1,2,3,4,5],[5,4,3,2,1],[6,7,8,9,10],[11,12,13,14,15]])
# y2 = array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,6],[1,2,3,4,5]])
# lables = [2,3,4,5]
# print(x1[:,1])
# type1 = ax.scatter(x1[:,1],y2[:,2],10*array(lables),10*array(lables))
plt.xlabel('玩视频游戏所消耗的时间百本比')
plt.ylabel('每年获取的飞行长客里程数')
plt.legend(loc='upper right')
plt.show()

# 矩阵中的三维数据 权重一致 所以 不会影响到其他计算
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
