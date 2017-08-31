from numpy import *
import operator

#训练数据
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0.1,0]])
    lables = ['A','A','B','B']
    return group,lables