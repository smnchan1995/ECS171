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


def read_clean_data():
    """
    This function will pull from the sqlite database 'jokedb.sqlite3' data
    related to the joke raters, joke ratings, and jokes themselves.
    It will minimally format the data, removing duplicate entries.

    It will return three DataFrames the first containing information
    regarding the joke raters, the second containing information about the
    joke ratings, and the third containing information about the jokes.

    joke_rater has columns:
    gender, age, birth_country, major, preferred_joke_genre,
    preferred_joke_genre2, preferred_joke_type, favorite_music_genre,
    favorite_movie_genre

    joke_ratings is a dataframe with columns indexing each joke and the row
    index being the index of the user rating the joke.

    jokes has columns:
    category, joke_type, subject, joke_text, joke_submitter_id, joke_source

    Returns:
        tuple(DataFrame, DataFrame, DataFrame): Three dataframes in order,
            joke raters, joke ratings, jokes
    """
    jokedb = sql.connect("jokedb.sqlite3")
    joke_rater = pd.read_sql_query("SELECT * from JokeRater", jokedb)
    joke = pd.read_sql_query("SELECT * from Joke", jokedb)
    joke_rating = pd.read_sql_query("SELECT * from JokeRating", jokedb)

    joke_rater = joke_rater.drop(['joke_submitter_id'], axis=1).set_index('id')

    joke = joke.set_index('id')
    joke_rating = joke_rating.drop_duplicates(['joke_id', 'joke_rater_id'],
                                            keep='first')
    pivot = joke_rating.pivot(index='joke_id', columns='joke_rater_id',
                              values='rating')
    joke_rating = pivot.transpose()

    return joke_rater, joke_rating, joke


def sample_jokes(jokes, n=5):
    """
    Right now our sampling procedure is to pick a random sample from the jokes
    """
    return [random.sample(jokes.index, n)]


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
            'biscaler', 'KNN', 'gauss'
    Returns:
        np.array: The completed matrix
    """
    if method == 'mean':
        imputer = fancyimputer.SimpleFill('mean')
    elif method == 'median':
        imputer = fancyimputer.SimpleFill('median')
    elif method == 'gauss':
        imputer = fancyimputer.SimpleFill('random')


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
    joke_raters, joke_ratings, jokes = read_clean_data()
    ratings_matrix = joke_ratings.values
    user = user.read_user()
    joke_ids = sample_jokes(jokes)

    joke_ratings = joke_ratings.append(pd.Series([np.nan]*len(joke_ratings.columns),
                                                 index=joke_ratings.columns),
                                       ignore_index=True)

    rating_field = IntegerField('rating', 1, 5)
    for joke_id in joke_ids:
        joke_text = jokes['joke_text'][joke_id]
        print("Please rate the following joke.")
        print(joke_text)
        rating = rating_field.read_input()
        joke_ratings[joke_id].iloc[-1] = rating

    ratings_matrix = joke_ratings.values

    completed_matrix = complete_matrix(ratings_matrix, method)

if __name__ == '__main__':
    main(sys.argv)
