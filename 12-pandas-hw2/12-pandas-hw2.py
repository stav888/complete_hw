import numpy as np
import pandas as pd


def main():
    people = pd.DataFrame({"name": ["Alice", "Bob", "Charlie", "Diana"], "age": [22, 35, 19, 40], "city": ["Paris", "London", "Berlin", "Paris"]})
    print("age > 30:\n", people[people.age > 30])
    print("Paris or London:\n", people[people.city.isin(["Paris", "London"])])
    print("age 20..25:\n", people[people.age.between(20, 25)])

    salaries = pd.DataFrame({"salary": [2500, 4000, 6000, 7500]})
    salaries["salary_tax"] = salaries.salary * 0.10
    salaries["annual_salary"] = salaries.salary * 12
    print(salaries)

    students = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "math": [80, 55, 90], "english": [70, 65, 85], "science": [60, 75, 95]})
    subjects = ["math", "english", "science"]
    students["total"] = students.apply(lambda row: row[subjects].sum(), axis=1)
    students["result"] = students[subjects].mean(axis=1).apply(lambda value: "Pass" if value > 60 else "Fail")
    print(students)

    rows = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
    rows.loc[len(rows)] = ["Charlie", 28]
    rows.iloc[1] = ["Bobby", 32]
    print(rows)

    cells = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "age": [22, 35, 28]})
    cells.at[0, "name"] = "Alicia"
    cells.iat[1, 1] = 36
    print(cells)

    df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df2 = pd.DataFrame({"A": [7, 8, 9], "B": [10, 11, 12]})
    print("concat by rows:\n", pd.concat([df1, df2], ignore_index=True))
    print("concat by columns:\n", pd.concat([df1, df2], axis=1))

    products = pd.DataFrame({"name": ["Book", "Pen", "Laptop", "Phone"], "price": [50, 10, 120, 80], "quantity": [5, 2, 10, 7]})
    print(products[products.price > 100])
    print(products[products.quantity.isin([5, 10])])
    print(products[products.price.between(50, 80)])

    departments = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"], "department": ["HR", "IT", "Finance"]})
    print(departments.drop(index=0).drop(columns="department"))

    books = pd.DataFrame({"title": ["1984", "Dune", "Dune", "Hamlet", "Hamlet", "Hamlet", "Emma"], "author": ["Orwell", "Herbert", "Herbert", "Shakespeare", "Shakespeare", "Shakespeare", "Austen"], "year": [1949, 1965, 1965, 1603, 1603, 1609, 1815]})
    print("duplicates:\n", books[books.duplicated()])
    print("last title occurrence:\n", books.drop_duplicates("title", keep="last"))

    missing = pd.DataFrame({"first_name": ["Liam", np.nan, "Noah", "Emma", "Olivia"], "last_name": ["Smith", np.nan, "Johnson", "Brown", "Wilson"], "age": [20, np.nan, 22, 19, 21], "major": ["Math", np.nan, "CS", "History", "Biology"], "gpa": [3.5, np.nan, np.nan, 3.7, 3.9], "credits": [30, np.nan, np.nan, 25, 40]})
    print("missing counts:\n", missing.isna().sum())
    missing["missing_count"] = missing.isna().sum(axis=1)
    print(missing[missing.gpa.isna() & missing.first_name.notna()])
    print(missing.fillna({"age": missing.age.mean(), "gpa": missing.gpa.min(), "credits": missing.credits.max()}))

    customers = pd.DataFrame({"cust_id": [1, 2, 3, 4], "name": ["Alice", "Bob", "Clara", "David"]})
    orders = pd.DataFrame({"order_id": [101, 102, 103, 104], "cust_id": [1, 2, 2, 5], "amount": [250, 400, 150, 500]})
    print(customers.merge(orders, on="cust_id", how="inner"))
    print(customers.merge(orders, on="cust_id", how="outer", indicator=True))


if __name__ == "__main__":
    main()
