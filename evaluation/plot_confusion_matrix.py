import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import f1_score

def read_data(file):
    corrects, incorrects = [], []
    for line in file:
        if line[0] == "[":
            content = line.replace('[', '').replace(']', '')
            corrects = list(map(float, content.split()))
        elif line[1] == "[":
            content = line.replace('[', '').replace(']', '')
            incorrects = list(map(float, content.split()))

    return [corrects, incorrects]


def plot_confusion_matrix(matrix, class_names):
    y_true = []
    y_pred = []
    num_classes = len(class_names)

    for i in range(num_classes):
        for j in range(num_classes):
            y_true += [i] * int(matrix[i][j])
            y_pred += [j] * int(matrix[i][j])
    f1 = f1_score(y_true, y_pred, average='micro')

    fig, ax = plt.subplots()
    cax = ax.matshow(matrix, cmap='YlOrRd')
    plt.colorbar(cax)

    if class_names is not None:
        ax.set_xticks(np.arange(num_classes))
        ax.set_yticks(np.arange(num_classes))
        ax.set_xticklabels(class_names)
        ax.set_yticklabels(class_names)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
    else:
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')

    # Annotate each cell with the numeric value
    for (i, j), val in np.ndenumerate(matrix):
        ax.text(j, i, int(val), ha='center', va='center', color='black')

    plt.title('Confusion Matrix', pad=50)
    plt.text(0.5, 1.15, f'F1 Score: {f1:.4f}', transform=ax.transAxes,
             ha='center', va='center', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(args[1], "confusion_matrix.png"))
    plt.show()


if __name__ == '__main__':
    args = sys.argv
    with open(os.path.join(args[1], "test.log"), mode="rt") as f:
        confusion_matrix = read_data(f)
    plot_confusion_matrix(confusion_matrix, ["correct", "knees_error"])