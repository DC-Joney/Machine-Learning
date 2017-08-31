from numpy import *
from KNN_demo import KNNFile,KNN2
result = tile([0,0],(2,2))
print(result)
distDemo = {0: 1}
print(distDemo.get(0,1))
returnMat,classLable = KNNFile.file2matrix("datingTestSet.txt")
