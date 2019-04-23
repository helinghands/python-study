## -*- coding: utf-8 -*-
#"""
#Created on Mon Apr  8 15:37:07 2019
##KNN分类器示例
#@author: hdk
#"""
#
#import numpy as np
#
#import matplotlib.pyplot as plt
#
#from sklearn import datasets
#
#from sklearn.model_selection import train_test_split
#
#from sklearn.neighbors import KNeighborsClassifier
#
#plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#
##step1准备数据集
#
#iris=datasets.load_iris()
#
#X=iris.data
#
#print('X:\n',X)
#
#Y=iris.target
#
#print('Y:\n',Y)
#
# 
#
##step2 数据预处理处理二分类问题，所以只针对Y=0,1的行，然后从这些行中取X的前两列
#
#x=X[Y<2,:2]
#
#print(x.shape)
#
#print('x:\n',x)
#
#y=Y[Y<2]
#
#print('y:\n',y)
#
##step3 样本可视化，target=0的点标红，target=1的点标蓝,点的横坐标为data的第一列，点的纵坐标为data的第二列
#
#plt.scatter(x[y==0,0],x[y==0,1],color='red')
#
#plt.scatter(x[y==1,0],x[y==1,1],color='green')
#
#plt.scatter(5.6,3.2,color='blue')
#
#x_1=np.array([5.6,3.2])
#
#plt.title('红色点标签为0,绿色点标签为1，待预测的点为蓝色')
##step4 样本划分
#x_train,x_test,y_train,y_test=train_test_split(x,y)
##step5 KNN建模
#knn_classifier=KNeighborsClassifier(6)
##step7 训练
#knn_classifier.fit(x_train,y_train)
##step8 测试
#y_predict=knn_classifier.predict(x_test)
##step9 分类性能指标
#scores=knn_classifier.score(x_test,y_test)
#print('acc:{}'.format(sum(y_predict==y_test)/len(x_test)),scores) 
#print("accuracy on the training subset:{:.3f}".format(knn_classifier.score(X_train,y_train)))
#print("accuracy on the test subset:{:.3f}".format(knn_classifier.score(x_test,y_test)))
#

def main():

    from sklearn import datasets

    digits=datasets.load_digits()

    x=digits.data

    y=digits.target

    from sklearn.model_selection import train_test_split

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=666)

    from sklearn.neighbors import KNeighborsClassifier

    # 寻找最好的k

    best_k=-1

    best_score=0

    for i in range(1,11):

        knn_clf=KNeighborsClassifier(n_neighbors=i)

        knn_clf.fit(x_train,y_train)

        scores=knn_clf.score(x_test,y_test)

        if scores>best_score:

            best_score=scores

            best_k=i

    print('最好的k为:%d,最好的得分为:%.4f'%(best_k,best_score))

if __name__ == '__main__':

    main()
