from numpy import *
import operator
from collections import Counter
def file2matrix(fileName):
    with open(fileName,'r') as fr:
        arrayLines = fr.readlines()
        count = len(arrayLines)
        returnMat = zeros((count,3))  #根据文本中的数据行数 初始化一个n,3的矩阵
        classLableVector = []
        index = 0
        for line in arrayLines:
            line = line.strip()
            lineDatas = line.split('\t')  #按照tab符号 来划分数据
            returnMat[index,:] = lineDatas[0:3]
            classLableVector.append(lineDatas[-1])
            index += 1
        dictClassLable = Counter(classLableVector)
        print(dictClassLable)
        classLable = []
        kind = list(dictClassLable)
        print(kind)
        for item in classLableVector:
            if item == kind[0]:
                item = 1
            elif item == kind[1]:
                item = 2
            else:
                item = 3
            classLable.append(item)
        return  returnMat,classLable


