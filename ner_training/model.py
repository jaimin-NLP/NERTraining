
from sklearn_crfsuite import CRF, metrics
from .utils import get_confusion_matrix

#Train a sequence model
def train_seq(X_train,Y_train,X_dev,Y_dev):
   # crf = CRF(algorithm='lbfgs', c1=0.1, c2=0.1, max_iterations=50, all_possible_states=True)
    crf = CRF(algorithm='lbfgs', c1=0.1, c2=10, max_iterations=50)#, all_possible_states=True)
    #Just to fit on training data
    crf.fit(X_train, Y_train)
    labels = list(crf.classes_)
    #testing:
    y_pred = crf.predict(X_dev)
    sorted_labels = sorted(labels, key=lambda name: (name[1:], name[0]))
    print(metrics.flat_f1_score(Y_dev, y_pred,average='weighted', labels=labels))
    print(metrics.flat_classification_report(Y_dev, y_pred, labels=sorted_labels, digits=3))