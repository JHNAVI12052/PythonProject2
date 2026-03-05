import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float).reshape(-1, 1)

    X_T = X.T
    theta = np.linalg.inv(X_T @ X) @ X_T @ y

    theta = np.round(theta, 4).flatten().tolist()



    return theta
print(linear_regression_normal_equation([[1,1],[1,2],[1,3]], [1,2,3]))


