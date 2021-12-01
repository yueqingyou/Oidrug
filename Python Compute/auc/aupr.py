import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import precision_recall_curve, average_precision_score


def ro_curve(y_pred, y_label, figure_file, method_name):
    y_label = np.array(y_label)
    y_pred = np.array(y_pred)
    lr_precision, lr_recall, _ = precision_recall_curve(y_label, y_pred)
    plt.plot(lr_recall, lr_precision, lw=2,
             label=method_name + ' (area = %0.3f)' % average_precision_score(y_label, y_pred))
    fontsize = 14
    plt.xlabel('Recall', fontsize=fontsize)
    plt.ylabel('Precision', fontsize=fontsize)
    plt.title('AUPR')
    plt.legend()
    plt.savefig(figure_file + ".png")
    return


def col_pic():
    for i in range(10):
        y_label = []
        y_pred = []
        with open("pre_lab_" + str(i) + ".csv") as f:
            f1 = csv.reader(f)
            for line in f1:
                y_label.append(float(line[0]))
                y_pred.append(float(line[1]))
            ro_curve(y_pred, y_label, "aupr_val_1", "Fold" + str(i + 1))


def main():
    col_pic()


if __name__ == "__main__":
    main()
