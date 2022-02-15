"""
Linear Regression
-----------------
Given a data matrix X and a response vector Y, find a linear model of best fit.

The linear model of best fit is given by the hyperplane that minimizes the least-squares
distance to the response vector Y.

Standard libraries and numpy only.

"""

from typing import Tuple

import numpy as np


def standardize(X: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns the standardized data matrix X (i.e. z-scores), as well as the means and
    standard deviations for each feature.
    """
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    scaled_X = (X - mu) / sigma
    return (scaled_X, mu, sigma)


class LinearRegression:
    """
    Given (n, m) data matrix X and (n,) continuous outcome vector Y, fits the parameters
    of a linear model to minimize least-squared error of the predictions.

    Provides two training interfaces:
        train() : fits parameters using iterative gradient descent
        train_svd() : fits parameters using the singular value decomposition of X
    """

    def train(
        self,
        X: np.ndarray,
        Y: np.ndarray,
        learning_rate: float = 0.005,
        num_epochs: int = 2000,
        loss_print_interval: int = 0,
    ):
        """
        Fits the model parameters to the given training data via gradient descent.

        Notes
        -----
        Given (n, m) data matrix X, and (m, 1) parameters B:
            y_hat = X • B

        Loss is MSE, or mean-squared error:
            L(B, X | Y) = (1 / n) * sum_i((y_hat - y)^2)

        The gradient of the loss with respect to each parameter B_j is given by:
            dL/dB_j = (1 / n) * sum_i((y_hat - y) * x_j)

        On parameter rescaling after fitting to standardized data:

        A linear regression on standardized data matrix X is given by standard form:
            y = B_0 + (X_1 • B_1) + ... + (X_j • B_j) + ... + (X_m • B_m)

        Let B_j' and X_j' denote the original, unscaled B_j and X_j, such that:
            X_j = (X_j' - mu_j) / sigma_j

        To find a formula for the unscaled B_j' terms, substitute in the z-score terms
        for each X_i and re-arrange to the standard form. A little algebra gives:
            B_0' = B_0 - sum_j(B_j' * mu_j / sigma_j)
            B_j' = B_j / sigma_j
        """
        n, m = X.shape
        assert Y.shape == (n,)

        # Scale and pad input features
        X_rescaled, mu, sigma = standardize(X)
        X_rescaled_padded = np.insert(arr=X_rescaled, obj=0, values=1, axis=1)

        # Randomly initialize parameters
        beta = np.random.random(size=m + 1)

        # Optimize parameters with gradient descent
        for epoch_idx in range(num_epochs):
            y_hat = X_rescaled_padded @ beta

            # Gradient w.r.t. to each parameter B_j
            gradient = np.mean((y_hat - Y).reshape(-1, 1) * X_rescaled_padded, axis=0)
            beta = beta + (-gradient * learning_rate)

            if loss_print_interval > 0 and epoch_idx % loss_print_interval == 0:
                # Loss is MSE
                loss = np.mean((y_hat - Y) ** 2)
                print(f"epoch = {epoch_idx:>5d}, loss = {loss:,.5f}")

        # Rescale parameters to the input space
        beta[0] = beta[0] - np.sum(beta[1:] * mu / sigma)
        beta[1:] = beta[1:] / sigma
        self.beta = beta

        return

    def train_svd(self, A: np.ndarray, b: np.ndarray):
        """
        Fits the regression parameters via SVD, or the singular value decomposition.

        Given equation Ax = b, where A = data, x = parameters, and b = response.

        Let the economy SVD of A be given by: SVD(A) = U S V^T
        Let A+ represent "A-dagger", or the left pseudo-inverse of A. Then:
            A+ = V S^-1 U^T

        Solving for x:
            Ax = b
            x~ = (A+) b
            x~ = (V S^-1 U^T) b

        Note: x~ is the best approximation of x given A.
        • for an under-determined system, x~ is the minimum L2 norm solution.
        • for an over-determined system, x~ is the least-squares solution.
        """
        A_padded = np.insert(arr=A, obj=0, values=1, axis=1)

        U, S, Vh = np.linalg.svd(A_padded, full_matrices=False)
        # x~ = (V S^-1 U^T) b
        x_tilde = Vh.T @ np.linalg.inv(np.diag(S)) @ U.T @ b
        self.beta = x_tilde
        return

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict the outcome for each observation in (n, m) data matrix X.
        """
        assert hasattr(self, "beta")
        X_padded = np.insert(arr=X, obj=0, values=1.0, axis=1)
        return X_padded @ self.beta


def test_standardize():
    from sklearn.preprocessing import StandardScaler

    n = 100
    X = np.c_[
        np.random.randint(100, 300, size=n),
        np.random.randint(10, 20, size=n),
    ]
    X_expected = StandardScaler().fit_transform(X)
    X_rescaled, mu, sigma = standardize(X)
    assert np.all(X_rescaled == X_expected)


def test_linear_regression():
    from sklearn.linear_model import LinearRegression as SKLinearRegression

    # Make a linear dataset, with some noise
    np.random.seed(0)
    n, m = 100, 2
    X = np.c_[
        np.random.randint(100, 300, size=n),
        np.random.randint(10, 20, size=n),
    ]
    X_padded = np.insert(arr=X, obj=0, values=1, axis=1)
    beta = np.array([100, 20, -100])
    Y = X_padded @ beta + np.random.normal(loc=0, scale=5, size=n)

    train_p = 0.8
    split_idx = int(train_p * n)
    X_train, X_test = X[:split_idx], X[split_idx:]
    Y_train, Y_test = Y[:split_idx], Y[split_idx:]

    # Train models
    model = LinearRegression()
    model.train(X=X_train, Y=Y_train)
    predictions = model.predict(X_test)

    model_svd = LinearRegression()
    model_svd.train_svd(A=X_train, b=Y_train)
    predictions_svd = model_svd.predict(X_test)

    sk_model = SKLinearRegression()
    sk_model.fit(X=X_train, y=Y_train)
    sk_predictions = sk_model.predict(X_test)

    # Validate parameters
    assert np.isclose(model.beta[0], sk_model.intercept_, atol=0.1)
    assert np.isclose(model_svd.beta[0], sk_model.intercept_, atol=0.1)
    assert np.allclose(model.beta[1:], sk_model.coef_, atol=0.1)
    assert np.allclose(model_svd.beta[1:], sk_model.coef_, atol=0.1)

    # Validate predictions
    assert np.allclose(sk_predictions, Y_test, rtol=0.01)
    assert np.allclose(predictions, sk_predictions, atol=1.0)
    assert np.allclose(predictions_svd, sk_predictions, atol=1.0)
