# -*- coding: utf-8 -*-
#Imports
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
import seaborn as sns


#Leitura da base de dados 
base = pd.read_csv("base_tratada.csv", sep=',')

#Descrição da base
print(base.describe())

#Remoção de colunas desnecessárias
del base["face_id"]

#Train test split
y = base["class"]
X_train, X_test, y_train, y_test = train_test_split(base, y, test_size=0.2, random_state=0)

#KNN
knn = KNeighborsClassifier()
params={'n_neighbors':[1,5,10,20,30,40,50,60,70,80,90,100], 'weights':('uniform', 'distance'), 'algorithm':('auto', 'ball_tree', 'kd_tree', 'brute'), 'leaf_size':[1,5,10,20,30,40,50,60,70,80,90,100], 'p':[1,2,3]  }
grid_search_knn = GridSearchCV(knn, param_grid=params, n_jobs=8, cv=5)

#Grid Search para obter melhores parametros
grid_search_knn.fit(X_train, y_train).predict(X_test)

#Treinamento KNN
knn = KNeighborsClassifier(**grid_search_knn.best_params_)

knn.fit(X_train,y_train)
y_pred_knn= knn.predict(X_test)

print(classification_report(y_pred_knn,y_test))


#Adabost
ada = AdaBoostClassifier()
params = {'n_estimators':[10,20,30,40,50,60,70,80,90,100], 'learning_rate':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0], 'algorithm':('SAMME','SAMME.R')}
grid_search_ada = GridSearchCV(ada ,params, n_jobs=8, cv=5)
grid_search_ada.fit(X_train, y_train).predict(X_test)

ada = AdaBoostClassifier(**grid_search_ada.best_params_)

ada.fit(X_train,y_train)
y_pred_ada= ada.predict(X_test) 

print(classification_report(y_pred_ada,y_test))

#SVM
svc = SVC()
params = {'kernel':('linear', 'poly', 'rbf'), 'coef0':[0.001,0.01,0.05,0.5,1],'C':[1,5,10,0.1,0.01],'gamma':[0.001,0.01,0.05,0.5,1]}
grid_search_svc = GridSearchCV(svc ,params, n_jobs=8, cv=5)

grid_search_svc.fit(X_train, y_train).predict(X_test)

svc = SVC(**grid_search_svc.best_params_)

svc.fit(X_train,y_train)
y_pred_svc= svc.predict(X_test) 

print(classification_report(y_pred_svc,y_test))

#Naive Bayes Gaussiano
gnb = GaussianNB(priors=None)

gnb.fit(X_train,y_train)
y_pred_gnb= gnb.predict(X_test) 

print(classification_report(y_pred_gnb,y_test))

#Arvore de Decisão
tree = DecisionTreeClassifier()

tree = DecisionTreeClassifier()
params = {'criterion':('gini', 'entropy'),'splitter':('best','random')}
grid_search_tree = GridSearchCV(tree ,params, n_jobs=8, cv=5)

grid_search_tree.fit(X_train, y_train).predict(X_test)

tree = DecisionTreeClassifier(**grid_search_tree.best_params_)

tree.fit(X_train,y_train)
y_pred_tree= tree.predict(X_test) 

print(classification_report(y_pred_tree,y_test))











