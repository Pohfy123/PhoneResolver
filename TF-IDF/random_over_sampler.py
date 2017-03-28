"""Class to perform random over-sampling."""

# Authors: Guillaume Lemaitre <g.lemaitre58@gmail.com>
#          Christos Aridas
# License: MIT
# https://github.com/scikit-learn-contrib/imbalanced-learn

from __future__ import division, print_function

from collections import Counter

import numpy as np
from sklearn.utils import check_random_state

from sklearn.utils import check_X_y

def random_over_sample(X, y, ratio='auto', random_state=None):
    X = np.array(X)
    y = np.array(y)

    # Create a dictionary containing the class statistics
    stats_c_ = Counter(y)

    # Find the minority and majority classes
    min_c_ = min(stats_c_, key=stats_c_.get)
    maj_c_ = max(stats_c_, key=stats_c_.get)

    # Keep the samples from the majority class
    X_resampled = X[y == maj_c_]
    y_resampled = y[y == maj_c_]

    # Loop over the other classes over picking at random
    for key in stats_c_.keys():

        # If this is the majority class, skip it
        if key == maj_c_:
            continue

        # Define the number of sample to create
        if ratio == 'auto':
            num_samples = int(stats_c_[maj_c_] - stats_c_[
                key])
        else:
            num_samples = int((ratio * stats_c_[maj_c_]) -
                              stats_c_[key])

        # Pick some elements at random
        random_state = check_random_state(random_state)
        indx = random_state.randint(
            low=0, high=stats_c_[key], size=num_samples)

        # Concatenate to the majority class
        X_resampled = np.concatenate(
            (X_resampled, X[y == key], X[y == key][indx]), axis=0)

        y_resampled = np.concatenate(
            (y_resampled, y[y == key], y[y == key][indx]), axis=0)

    return X_resampled, y_resampled
