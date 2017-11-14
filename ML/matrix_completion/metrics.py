"""
metrics.py

This module will provide some basic metrics for evaluating the performance
of the separate methods for filling in the matrices.
"""

import random
import numpy as np

import matrix_complete

def mean_square_error(actuals, predicteds):
    """
    This will compute the mean square error of the data.
    This is defined as
        MSE = ((x1 - y1)^2 + ... + (xn - yn)^2)/n

    Args:
        actuals (list[float]): The list of actual observed values
        predicteds (list[float]): The list of predicted values
    Returns:
        float: The mean square error
    """
    xs = np.array(actuals)
    ys = np.array(predicteds)
    return np.mean((xs - ys) ** 2)


class Tester:
    def __init__(self, sampler='simple', matrix_picker='simple',
                 completer='mean'):
        self.sampler = sampler
        self.picker = matrix_picker
        self.completer = completer

    def test(self, matrix):
        chosen_submatrix = self.pick(matrix)
        m, n = chosen_submatrix.shape
        row_index = random.choice(list(range(m))

        # These are the indices of the columns we'll keep.
        # In the algorithm, these would be the jokes we recommend to the user
        # initially.
        col_indices = self.sample(chosen_submatrix)
        matrix_copy = chosen_submatrix.copy
        actual_row = matrix_copy[row_index]

        row_copy = row.copy()
        for index in range(n):
            if index not in col_indices:
                row_copy[index] = np.nan

        matrix_copy[row_index] = row_copy
        complete_matrix = self.complete(matrix_copy)
        predicted_row = complete_matrix[row_index]
        self.mse = mean_square_error(actual_row, predicted_row)
        self.print_report()

    def sample(self, matrix):
        m, n = matrix.shape
        if self.sampler == 'simple':
            return random.sample(list(range(matrix.shape[1])), 5)
        else:
            print("Alternative methods not implemented yet")
            raise NotImplementedError

    def pick(self, matrix):
        m, n = matrix.shape
        if self.picker == 'simple':
            return matrix
        else:
            print("Alternative methods not implemented yet")
            raise NotImplementedError

    def complete(matrix):
        return matrix_complete.complete_matrix(matrix, self.method)

    def print_report(self):
        print("Results for test using {} sampler, {} picker, {} completer"
            .format(self.sampler, self.picker, self.

def test_method(matrix, method):
    """
    This method will select a random row and delete all but 5 entries from it.
    It will use then complete the matrix with this incomplete row.
    It will then compute the mean square error between the actual row and the
    predicted row.

    Args:
        matrix (np.array): The matrix with possibly incomplete values
        method (str): The method for matrix completion
    Returns:
        float: The mean squared error of the row
    """
    m, n = matrix.shape
    row_index = random.choice(list(range(m)))
    
    matrix_copy = matrix.copy()

    actual_row = matrix[row_index]
    row_copy = actual_row.copy()
    
    for index in random.sample(list(range(n)), n - 5):
        row_copy[index] = np.nan
    matrix_copy[row_index] = row_copy
    complete_matrix = matrix_complete.complete_matrix(matrix_copy, method)
    predicted_row = complete_matrix[row_index]

    return mean_square_error(actual_row, predicted_row)
