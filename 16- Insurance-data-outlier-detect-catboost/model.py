"""
Import



"""

from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC


from sklearn.ensemble import AdaBoostClassifier


def export(X, y , random_state = 0 , n_neighbors= 30, n_estimators = 100 , max_depth = 2 , svc_n_estimators = 20):
    # SVC
    svc_model = SVC(gamma='auto')
    svc_clf = SVC(gamma='auto').fit(X, y )

    # KNN Classifier
    knn_clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)


    # Tree
    tree_clf = DecisionTreeClassifier(random_state=random_state).fit(X, y)

    # random forest
    random_forest_clf = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state).fit(X, y)

    # EXtra Tree
    extra_tree_clf = ExtraTreesClassifier(n_estimators=n_estimators, random_state=random_state).fit(X, y)


    
    # return
    return {
        'svc_clf':svc_clf,
        'knn_clf':knn_clf,
        'tree_clf':tree_clf,
        'random_forest_clf':random_forest_clf,

    }

from sklearn.metrics import accuracy_score,confusion_matrix
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import itertools
def status(models,x_train , y_train, x_test , y_test,lables, data_type = '', normalize = False):
    def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)
        plt.show()
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        print(cm)

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()
    
    for key, model in models.items():
        print("""
        model : {}
        """.format(key))
        pred_train = model.predict(x_train)
        pred_test = model.predict(x_test)
        print("{} - {}: training accuracy={:.2%}, test accuracy={:.2%}".format(data_type,key,
           accuracy_score(pred_train, y_train),
          accuracy_score(pred_test,y_test)))
        
        y_pred = pred_test
        cnf_matrix = confusion_matrix(y_test, y_pred)
        np.set_printoptions(precision=2)
        plot_confusion_matrix(cnf_matrix, classes=lables,
                      title='Confusion matrix for '.format(key) , normalize = normalize)
        
        
from sklearn.model_selection import GridSearchCV

def best_param(X, y):
    #
    # SVC
    parameters = {'kernel':('linear', 'rbf'), 'C':np.arange(1, 5)}
    svc_clf = GridSearchCV(SVC(), parameters, cv = 2 , n_jobs = -1).fit(X, y )
    print("""
    params : {}
    model : svc_clf
    best param : {} 
    """.format( parameters, svc_clf.best_params_))
    

    # KNN Classifier
    parameters = {'n_neighbors': np.arange(5, 25)} #, 'weights':['uniform','distance'], 'metric':['euclidean','manhattan']}
    knn_clf = GridSearchCV(KNeighborsClassifier(), parameters , cv = 3 , n_jobs = -1).fit(X, y )
    print("""
    params : {}
    model : knn_clf
    best param : {} 
    """.format( parameters, knn_clf.best_params_))
          

