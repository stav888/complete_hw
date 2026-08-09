"""Logistic regression exercise using brisk-activity minutes and a 10k-step outcome."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


def main():
    minutes = np.array([5, 12, 18, 22, 28, 35, 42, 48, 55, 63, 72, 85]).reshape(-1, 1)
    reached_10k = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
    model = LogisticRegression(solver="liblinear").fit(minutes, reached_10k)
    probabilities = model.predict_proba(minutes)[:, 1]
    predictions = model.predict(minutes)
    print("intercept:", model.intercept_[0])
    print("coefficient:", model.coef_[0, 0])
    print("confusion matrix:\n", confusion_matrix(reached_10k, predictions))
    print(f"accuracy: {accuracy_score(reached_10k, predictions) * 100:.2f}%")
    confidence_70 = np.log(0.7 / 0.3) / model.coef_[0, 0] - model.intercept_[0] / model.coef_[0, 0]
    print(f"minutes for 70% confidence: {confidence_70:.2f}")
    probability_at_46 = model.predict_proba([[46]])[0, 1]
    prediction_at_46 = int(model.predict([[46]])[0])
    print(f"probability at x=46: {probability_at_46:.4f}")
    print(f"prediction for x=46: {prediction_at_46}")
    grid = np.linspace(minutes.min(), minutes.max(), 200).reshape(-1, 1)
    plt.scatter(minutes, reached_10k, label="observations")
    plt.plot(grid, model.predict_proba(grid)[:, 1], label="logistic curve")
    plt.axvline(confidence_70, color="red", linestyle="--", label="70% boundary")
    plt.xlabel("Brisk-activity minutes")
    plt.ylabel("Probability of reaching 10,000 steps")
    plt.legend()
    plt.tight_layout()
    plt.savefig("logistic_regression.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
