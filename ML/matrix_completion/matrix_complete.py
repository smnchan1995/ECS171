"""
matrix_complete.py

This program purports to implement a matrix completion algorithmic approach
to the recommender problem. To that end it will construct a matrix where the
rows are indexed by joke and columns are indexed by users
"""

import sys
import sqlite3 as sql
import random

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import fancyimpute

import user
from forms import IntegerField, CategoricalField

class User:
    """
    Simple Representation of a user
    This just has all the fields that are in the user profile
    """
    def __init__(self, gender, age, birth_country, major, joke_genre,
                 joke_genre2, joke_type, music, movie):
        self.gender = gender
        self.age = age
        self.birth_country = birth_country
        self.major = major
        self.joke_genre = joke_genre
        self.joke_genre2 = joke_genre2
        self.joke_type = joke_type
        self.music = music
        self.movie = movie


def sample_jokes(jokes, n=5):
    """
    Right now our sampling procedure is to pick a random sample from the jokes
    """   
    categories = list(jokes['category'].unique())

    for i in range(len(categories)):
        temp =  jokes[jokes['category'] == categories[i]]
        print(temp.sample(n=1).index)

    return random.sample(jokes.index.tolist(), n)

def modify_jokes(joke):
    joke.columns = ['category', 'joke_type', 'subject', 'joke_text', 'joke_submitter_id', 'joke_source']

    del joke['subject']
    del joke['joke_text']
    del joke['joke_submitter_id']
    del joke['joke_source']

    joke = joke.sort_values(by=['category'])

    return joke

def complete_matrix(matrix, method):
    """
    This method will complete the matrix based on the method specified.
    This will not change the matrix in place instead constructing a new matrix
    with the completed entries.

    Args:
        matrix (np.array): A numpy array with nan entries representing
            missing entries
        method (str): One of 'mean', 'median', 'soft_impute', 'iterativeSVD',
            'MICE', 'matrix_factorization', 'nuclear_norm_minimization',
            'KNN', 'gauss'
    Returns:
        np.array: The completed matrix
    """
    if method == 'mean':
        imputer = fancyimpute.SimpleFill('mean')
    elif method == 'median':
        imputer = fancyimpute.SimpleFill('median')
    elif method == 'gauss':
        imputer = fancyimpute.SimpleFill('random')
    elif method == 'soft_impute':
        imputer = fancyimpute.SoftImpute()
    elif method == 'iterativeSVD':
        imputer = fancyimpute.IterativeSVD()
    elif method == 'MICE':
        imputer = MICE()
    elif method == 'matrix_factorization':
        imputer = MatrixFactorization()
    elif method == 'nuclear_norm_minimization':
        imputer = NuclearNormMinimization()
    elif method == 'KNN':
        imputer = KNN()
    else:
        raise ValueError("Unrecognized method passed in")

    return imputer.complete(matrix)


def main(argv=None):
    """
    The algorithm is simple:
        1. Read In Data
        2. Prepare Matrix
        3. Read in User
        4. Sample Jokes to give to User
        5. Add a Column of User Response to joke
        6. Apply Matrix Completion to get predicted ratings
        7. Use these to suggest new jokes
    """
    joke_raters, joke_ratings, jokes = user.read_clean_data()
    
    ratings_matrix = joke_ratings.values
    new_user = user.read_user()
    joke_ids = sample_jokes(jokes)

    joke_ratings = joke_ratings.append(pd.Series([np.nan]*len(joke_ratings.columns),
                                                 index=joke_ratings.columns),
                                       ignore_index=True)

    rating_field = IntegerField('rating', 1, 5)
    print(joke_ids)
    for joke_id in joke_ids:
        joke_text = jokes['joke_text'][joke_id]
        print("Please rate the following joke.")
        print(joke_text)
        rating = rating_field.read_input()
        joke_ratings[joke_id].iloc[-1] = rating

    ratings_matrix = joke_ratings.values

    completed_matrix = complete_matrix(ratings_matrix, 'mean')

    print(completed_matrix)

if __name__ == '__main__':
    main(sys.argv)
