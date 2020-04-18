"""
Import



"""

from sklearn.metrics import accuracy_score,confusion_matrix
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import itertools
def status(model,x_train , y_train, x_test , y_test,lables, data_type = '', normalize = False):
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
    


    pred_train = model.predict(x_train)
    pred_test = model.predict(x_test)
    print("{} -: training accuracy={:.2%}, test accuracy={:.2%}".format(data_type,
    accuracy_score(pred_train, y_train),
    accuracy_score(pred_test,y_test)))
        
    y_pred = pred_test
    cnf_matrix = confusion_matrix(y_test, y_pred)
    np.set_printoptions(precision=2)
    plot_confusion_matrix(cnf_matrix, classes=lables,
    title='Confusion matrix for '.format(data_type) , normalize = normalize)
        
 

