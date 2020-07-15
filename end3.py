# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 23:11:30 2020
绘制四种算法对比图
@author: 70951
"""


import numpy as np
import matplotlib.pyplot as mp

# 设置中文字体
mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False

SGD = np.array([0.86285, 0.8832 , 0.84545])
Random_forest = np.array([0.9289 , 0.92275, 0.9309 ])
GaussianNB = np.array([0.5592 , 0.56035, 0.55715])
BernoulliNB = np.array([0.79514097, 0.84068407, 0.8319832 ])
SVM = np.array([0.8491 , 0.8412 , 0.85925])

SGD = np.append(SGD,np.mean(SGD))
Random_forest = np.append(Random_forest,np.mean(Random_forest))
GaussianNB = np.append(GaussianNB,np.mean(GaussianNB))
BernoulliNB = np.append(BernoulliNB,np.mean(BernoulliNB))
SVM = np.append(SVM,np.mean(SVM))

apples = np.array([45, 46, 12, 45, 121, 65, 45, 60, 11, 56, 34, 54])
oranges = np.array([54, 36, 82, 47, 96, 34, 45, 62, 85, 66, 94, 63])
mp.figure('算法准确度对比分析')
mp.title('Comparative analysis of algorithm accuracy', fontsize=16)
mp.xlabel('Algorithm', fontsize=14)
mp.ylabel('Probability', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':', axis='y')
x = np.arange(4)
x = 2*x
a = mp.bar(x - 0.5, SGD, 0.2, color='dodgerblue', label='SGD', align='center')
b = mp.bar(x - 0.3, Random_forest, 0.2, color='orangered', label='Random_forest', align='center')
c = mp.bar(x - 0.1, GaussianNB, 0.2, color='c', label='GaussianNB', align='center')
d = mp.bar(x + 0.1, BernoulliNB, 0.2, color='red', label='BernoulliNB', align='center')
e = mp.bar(x + 0.3, SVM, 0.2, color='green', label='SVM', align='center')
# 设置标签
for i in a + b + c + d + e:
    h = i.get_height()
    mp.text(i.get_x() + i.get_width() / 2, h, '%.4g' % float(h), ha='center', va='bottom')
mp.xticks(x, ['1_Fold', '2_Fold', '3_Fold', 'Mean'])

mp.legend()
mp.ylim(0,1.5)
mp.show()
