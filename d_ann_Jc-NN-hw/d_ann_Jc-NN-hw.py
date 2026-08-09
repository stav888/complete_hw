import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression


def main():
    rooms = np.array([2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
    prices = np.array([900, 1200, 1500, 1800, 2100, 2400, 2700])
    linear_model = LinearRegression().fit(rooms, prices)
    print("price for 5.5 rooms:", linear_model.predict([[5.5]])[0])

    experience = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
    discount = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
    logistic_model = LogisticRegression(solver="liblinear").fit(experience, discount)
    print("discount probability at 6.5 years:", logistic_model.predict_proba([[6.5]])[0, 1])


if __name__ == "__main__":
    main()
