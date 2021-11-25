"""
Logistic Regression
-------------------
Learn a generalized linear model for binary classification given data matrix X and
binary outcomes Y.

Standard libraries and numpy only.

"""

from typing import Tuple

import numpy as np
from scipy.special import expit


def standardize(X: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns the standardized data matrix X (i.e. z-scores), as well as the means and
    standard deviations for each feature.
    """
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    scaled_X = (X - mu) / sigma
    return (scaled_X, mu, sigma)


class LogisticRegression:
    """
    Given (n, m) data matrix X and (n,) binary outcome vector Y, fits the parameters of
    a logistic regression model to minimize negative log likelihood of the predictions.
    """

    def train(
        self,
        X: np.ndarray,
        Y: np.ndarray,
        learning_rate: float = 0.01,
        max_num_epochs: float = float("inf"),
        loss_convergence_threshold: float = 0.0001,
        loss_print_interval: int = -1,
    ):
        """
        Fits the model parameters to the given training data via gradient descent.

        Notes
        -----
        Given (n, m) data matrix X, and (m, 1) parameters B:
            p_hat = sigmoid(X • B)

        i.e. the conditional probability for a given observation x and label y:
            P(y | B, x) = sigmoid(x • B)        if y == 1
                        = 1 - sigmoid(x • B)    if y == 0

        Loss is total negative log likelihood:
            L(B, X | Y) = -sum_i((y * log(p_hat)) + (1 - y) * log(1 - p_hat))

        The gradient with respect to each parameter B_j is given by:
            dL/dB_j = (1 / n) * sum_i((p_hat - y) * x_j)

        n.b.: the gradient is identical to the gradient for least-squares regression.
        """
        n, m = X.shape
        assert Y.shape == (n,)

        # Scale and pad input features
        X_rescaled, mu, sigma = standardize(X)
        X_rescaled_padded = np.insert(arr=X_rescaled, obj=0, values=1, axis=1)

        # Randomly initialize parameters
        beta = np.random.random(size=m + 1)

        # Optimize parameters with gradient descent
        last_loss = float("inf")
        epoch_idx = 1
        while epoch_idx < max_num_epochs:
            p_hat = expit(X_rescaled_padded @ beta)

            # Gradient w.r.t. each parameter B_j
            gradient = np.mean((p_hat - Y).reshape(-1, 1) * X_rescaled_padded, axis=0)
            beta = beta + (-gradient * learning_rate)

            # Loss is total negative log likelihood
            loss = np.sum(np.where(Y == 1, -np.log(p_hat), -np.log(1 - p_hat)))
            if abs(last_loss - loss) < loss_convergence_threshold:
                print(f"Converged after {epoch_idx} iterations, loss = {loss}")
                break

            if loss_print_interval > 0 and epoch_idx % loss_print_interval == 0:
                print(f"epoch = {epoch_idx:>5d}, loss = {loss:,.5f}")

            last_loss = loss
            epoch_idx += 1

        # Rescale parameters to the input space
        beta[0] = beta[0] - np.sum(beta[1:] * mu / sigma)
        beta[1:] = beta[1:] / sigma
        self.beta = beta

        return

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict the probability of label 1 for each observation in (n, m) data matrix X.
        """
        assert hasattr(self, "beta")
        X_padded = np.insert(arr=X, obj=0, values=1, axis=1)
        return expit(X_padded @ self.beta)


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


def test_logistic_regression():
    from sklearn.linear_model import LogisticRegression as SKLogisticRegression
    from sklearn.metrics import roc_auc_score

    # Make a linear dataset, with some noise
    np.random.seed(0)
    n, m = 100, 2
    X = np.c_[
        np.random.randint(100, 300, size=n),
        np.random.randint(10, 20, size=n),
    ]
    X_padded = np.insert(arr=X, obj=0, values=1, axis=1)
    beta = np.array([4, 10, -100])
    Y_ = X_padded @ beta + np.random.normal(loc=0, scale=5, size=n)
    Y = (Y_ > np.mean(Y_)).astype(np.int8)

    train_p = 0.8
    split_idx = int(train_p * n)
    X_train, X_test = X[:split_idx], X[split_idx:]
    Y_train, Y_test = Y[:split_idx], Y[split_idx:]

    # Train models
    model = LogisticRegression()
    model.train(
        X=X_train,
        Y=Y_train,
        learning_rate=0.1,
        loss_convergence_threshold=0.0001,
    )
    predictions = model.predict(X_test)

    sk_model = SKLogisticRegression()
    sk_model.fit(X=X_train, y=Y_train)
    sk_predictions = sk_model.predict(X_test)

    # Validate parameters
    assert np.isclose(model.beta[0], sk_model.intercept_, atol=5.0)
    assert np.allclose(model.beta[1:], sk_model.coef_, atol=0.5)

    # Validate predictions
    auc = roc_auc_score(Y_test, predictions)
    sk_auc = roc_auc_score(Y_test, sk_predictions)
    assert sk_auc > 0.9
    assert auc > 0.9
    predicted_positives = predictions > 0.5
    sk_predicted_positives = sk_predictions > 0.5
    assert np.sum(predicted_positives != sk_predicted_positives) <= 1
