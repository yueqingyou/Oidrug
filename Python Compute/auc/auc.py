import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc


def ro_curve(y_pred, y_label, figure_file, method_name):
    y_label = np.array(y_label)
    y_pred = np.array(y_pred)
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    fpr[0], tpr[0], _ = roc_curve(y_label, y_pred)
    roc_auc[0] = auc(fpr[0], tpr[0])
    lw = 2
    plt.plot(fpr[0], tpr[0],
             lw=lw, label=method_name + ' (area = %0.2f)' % roc_auc[0])
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    fontsize = 14
    plt.xlabel('False Positive Rate', fontsize=fontsize)
    plt.ylabel('True Positive Rate', fontsize=fontsize)
    plt.title('AUROC', fontsize=fontsize)
    plt.legend(loc="lower right")
    plt.savefig(figure_file + ".png")
    return


def col_pic():
    for i in range(10):
        y_label = []
        y_pred = []
        with open("pre_lab_" + str(i) + ".csv") as f:
            f1 = csv.reader(f)
            for line in f1:
                y_label.append(int(float(line[0])))
                y_pred.append(float(line[1]))
            ro_curve(y_pred, y_label, "auc_val_1", "Fold" + str(i + 1))


def main():
    col_pic()


if __name__ == "__main__":
    main()
