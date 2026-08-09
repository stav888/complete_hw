import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text


def main():
    x = np.array([[20, 4], [22, 5], [25, 6], [30, 10], [32, 12], [35, 14], [40, 18], [45, 20], [48, 22], [52, 25], [55, 28], [60, 30], [62, 32], [65, 35], [70, 40], [30, 10], [45, 20], [60, 30], [18, 3], [21, 4], [24, 5], [28, 9], [33, 11], [36, 15], [25, 6], [55, 28], [40, 18], [68, 38], [72, 42], [66, 36]])
    y = np.array(["cat", "cat", "cat", "dog", "dog", "dog", "dog", "dog", "dog", "horse", "horse", "horse", "horse", "horse", "horse", "cat", "horse", "dog", "cat", "cat", "cat", "dog", "dog", "dog", "dog", "dog", "horse", "horse", "horse", "horse"])
    for test_size in (0.2, 0.3, 0.4):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=42, stratify=y)
        model = DecisionTreeClassifier(max_depth=3, random_state=42).fit(x_train, y_train)
        print(f"split={int((1-test_size) * 100)}/{int(test_size * 100)}")
        print("accuracy:", accuracy_score(y_test, model.predict(x_test)))
        print("confusion matrix:\n", confusion_matrix(y_test, model.predict(x_test), labels=model.classes_))
        print(export_text(model, feature_names=["length", "weight"]))
    final_model = DecisionTreeClassifier(max_depth=3, random_state=42).fit(x, y)
    print("prediction for [34, 17]:", final_model.predict([[34, 17]])[0])


if __name__ == "__main__":
    main()
