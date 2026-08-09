import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC


def main():
    apples = np.array([[3, 150], [4, 130], [2, 160], [3, 140], [3.5, 145]])
    bananas = np.array([[7, 120], [6, 110], [8, 115], [7.5, 125], [6.5, 118]])
    x = np.vstack([apples, bananas])
    y = np.array([-1] * len(apples) + [1] * len(bananas))
    model = SVC(kernel="linear").fit(x, y)
    predictions = model.predict(x)
    print("coefficients:", model.coef_)
    print("intercept:", model.intercept_)
    print("confusion matrix:\n", confusion_matrix(y, predictions, labels=[-1, 1]))
    print("accuracy:", accuracy_score(y, predictions))
    plt.scatter(x[y == -1, 0], x[y == -1, 1], label="apple")
    plt.scatter(x[y == 1, 0], x[y == 1, 1], label="banana")
    weights = model.coef_[0]
    intercept = model.intercept_[0]
    x_values = np.linspace(x[:, 0].min(), x[:, 0].max(), 200)
    boundary = -(weights[0] * x_values + intercept) / weights[1]
    margin = 1 / np.linalg.norm(weights)
    plt.plot(x_values, boundary, "k-", label="decision boundary")
    plt.plot(x_values, boundary + margin, "k--", label="margins")
    plt.plot(x_values, boundary - margin, "k--")
    plt.xlabel("Size")
    plt.ylabel("Weight (g)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("svm_apples_bananas.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
