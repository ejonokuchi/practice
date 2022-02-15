"""
Stochastic Testing
------------------
Simple methods for validating stochastic functions using hypothesis tests.

"""

import math
import random
from typing import Any, Counter, Dict

from scipy.stats import binomtest, chisquare, norm


def bernoulli(p: float = 0.5) -> bool:
    """
    Samples from a Bernoulli distribution, given a probability of success p.

    Returns True if the trial was a success.
    """
    return random.random() < p


class Categorical:
    """
    Builds a categorical distribution given a dictionary d, mapping keys to their
    relative weights. Weights need not be normalized.
    """

    def __init__(self, d: Dict[Any, float]):
        self.keys, self.cdf = self._build_dist(d)

    def _build_dist(self, d: Dict[Any, float]):
        """
        Builds a cdf table given keys with unnormalized weights.

        Returns the ordering of the keys in the cdf, as well as the cdf table.
        """
        # get a stable ordering of keys
        keys = list(d.keys())
        # construct cumulative distribution
        total = sum(d.values())
        cume_dist = 0
        for k in keys:
            cume_dist += d[k] / total
            d[k] = cume_dist
        return keys, d

    def sample(self):
        """
        Returns k from d with probability d[k]/total_weights.
        """
        x = random.random()
        for k in self.keys:
            if x < self.cdf[k]:
                return k


def test_bernoulli_even():
    """
    Two-tailed Z-test for proportion. Fails with probability alpha = .01.
    """
    n = 1000
    p = 0.5
    alpha = 0.01

    samples = [bernoulli(p=p) for _ in range(n)]
    p_hat = sum(samples) / n

    z = (p_hat - p) / math.sqrt(p * (1 - p) / n)
    p_value = norm.sf(abs(z)) * 2
    assert not p_value < alpha


def test_bernoulli_uneven():
    """
    Binomial exact test, where the probability of success p is close to 0, making the
    normal approximation invalid.

    Fails with probability alpha = .01.
    """
    n = 1000
    p = 0.003
    alpha = 0.01

    samples = [bernoulli(p=p) for _ in range(n)]
    k = sum(samples)

    test = binomtest(k=k, n=n, p=p, alternative="two-sided")
    assert not test.pvalue < alpha


def test_categorical_normalized():
    """
    Pearson's chi-squared test for goodness of fit.

    Fails with probability alpha = .01.
    """
    n = 1000
    d = {
        "a": 0.25,
        "b": 0.25,
        "c": 0.5,
    }
    alpha = 0.01

    dist = Categorical(d.copy())
    keys = dist.keys
    counts_obs = Counter([dist.sample() for _ in range(n)])

    total = sum(d.values())
    counts_exp = {k: (v / total) * n for k, v in d.items()}

    test = chisquare(
        f_obs=[counts_obs[k] for k in keys],
        f_exp=[counts_exp[k] for k in keys],
    )
    assert not test.pvalue < alpha


def test_categorical_unnormalized():
    """
    Pearson's chi-squared test for goodness of fit.

    Fails with probability alpha = .01.
    """
    n = 1000
    d = {
        "a": 6,
        "b": 2,
        "c": 12,
    }
    alpha = 0.01

    dist = Categorical(d.copy())
    keys = dist.keys
    counts_obs = Counter([dist.sample() for _ in range(n)])

    total = sum(d.values())
    counts_exp = {k: (v / total) * n for k, v in d.items()}

    test = chisquare(
        f_obs=[counts_obs[k] for k in keys],
        f_exp=[counts_exp[k] for k in keys],
    )
    assert not test.pvalue < alpha
