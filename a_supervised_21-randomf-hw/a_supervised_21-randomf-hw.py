import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def main():
    # Features: height, weight, ear length; labels are animal classes.
    x = np.array([[25, 3.5, 8], [30, 4.2, 9], [28, 3.8, 8.5], [50, 18, 12], [55, 22, 13], [48, 16.5, 11], [150, 450, 60], [140, 420, 58], [160, 480, 62], [52, 20, 12.5]])
    y = np.array(["cat", "cat", "cat", "dog", "dog", "dog", "horse", "horse", "horse", "dog"])
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=42).fit(x_train, y_train)
    print("accuracy:", accuracy_score(y_test, model.predict(x_test)))
    print("OOB score:", model.oob_score_)
    print("prediction for [45, 12, 10]:", model.predict([[45, 12, 10]])[0])


if __name__ == "__main__":
    main()
