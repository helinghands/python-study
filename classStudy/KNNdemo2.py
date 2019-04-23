# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:03:03 2019

@author: hdk
"""

import numpy as np
from sklearn import metrics
from sklearn.metrics import roc_curve, auc,roc_auc_score  ###计算roc和auc
  
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import mglearn
import matplotlib.pyplot as plt
  
cancer=load_breast_cancer()
  
#mglearn.plots.plot_knn_classification(n_neighbors=3)
X_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,stratify=cancer.target,random_state=42)
  
knn=KNeighborsClassifier()
knn.fit(X_train,y_train)
print("accuracy on the training subset:{:.3f}".format(knn.score(X_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(knn.score(x_test,y_test)))
  
#Auc验证，数据采用测试集数据
#癌症的概率
proba_cancer=knn.predict_proba(x_test)
y_scores=pd.DataFrame(proba_cancer)[1]
y_scores=np.array(y_scores)
y_true=y_test
#auc分数
#auc分数有两种计算方式，第一种是根据目标变量y_true,预测分数/预测概率y_socres,通过roc_auc_score(y_true, y_scores)计算AUC
AUC=roc_auc_score(y_true, y_scores)
print("AUC:",AUC)
#auc第二种方法是通过fpr,tpr，通过auc(fpr,tpr)来计算AUC
fpr, tpr, thresholds = metrics.roc_curve(y_true, y_scores, pos_label=1)
AUC1 = auc(fpr,tpr) ###计算auc的值 
  
#print("fpr:",fpr)
#print("tpr:",tpr)
#print("thresholds:",thresholds)
print("AUC1:",AUC1)
  
if AUC >=0.7:
    print("good classifier")
if 0.7>AUC>0.6:
    print("not very good classifier")
if 0.6>=AUC>0.5:
    print("useless classifier")
if 0.5>=AUC:
    print("bad classifier,with sorting problems")
      
  
#绘制ROC曲线
#画对角线 
plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Diagonal line') 
plt.plot(fpr,tpr,label='ROC curve (area = %0.2f)' % AUC) 
plt.title('ROC curve')  
plt.legend(loc="lower right")   