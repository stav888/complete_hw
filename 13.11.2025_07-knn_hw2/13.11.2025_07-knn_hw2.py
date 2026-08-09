"""Manual and scikit-learn KNN regression."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor


def manual_knn_predict(x_train, y_train, query, k=3):
    distances = np.linalg.norm(x_train - query, axis=1)
    nearest = np.argsort(distances)[:k]
    return float(np.mean(y_train[nearest])), nearest, distances[nearest]


def main():
    rng = np.random.default_rng(42)
    x_data = np.array([[0.5, 1.0, 0.2], [1.0, 1.5, 0.4], [1.5, 2.0, 0.6], [2.0, 2.5, 0.8], [2.5, 3.0, 1.0], [3.0, 3.5, 1.3], [3.5, 4.0, 1.5], [4.0, 4.5, 1.8]])
    y_data = np.array([2.1, 2.8, 3.5, 4.2, 4.9, 5.7, 6.4, 7.2])
    query = np.array([2.7, 3.2, 1.1])
    manual_prediction, neighbors, neighbor_distances = manual_knn_predict(x_data, y_data, query)
    print("manual query:", query)
    print("manual neighbors:", neighbors.tolist())
    print("manual distances:", neighbor_distances.tolist())
    print("manual prediction:", manual_prediction)
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=42)
    manual_predictions = np.array([manual_knn_predict(x_train, y_train, value)[0] for value in x_test])
    print("manual k=3 MSE:", mean_squared_error(y_test, manual_predictions))
    x = rng.uniform(0, 10, size=(100, 3))
    y = 2 * x[:, 0] + 0.5 * x[:, 1] - x[:, 2] + rng.normal(0, 1, 100)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    ks = range(3, 10)
    errors = []
    for k in ks:
        model = KNeighborsRegressor(n_neighbors=k).fit(x_train, y_train)
        errors.append(mean_squared_error(y_test, model.predict(x_test)))
    for k, error in zip(ks, errors):
        print(f"k={k}: MSE={error:.4f}")
    best_k = list(ks)[int(np.argmin(errors))]
    print("best k:", best_k)
    plt.plot(list(ks), errors, marker="o")
    plt.xlabel("k")
    plt.ylabel("Mean squared error")
    plt.title("KNN regression model selection")
    plt.tight_layout()
    plt.savefig("knn_mse.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
