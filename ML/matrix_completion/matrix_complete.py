"""
matrix_complete.py

This program purports to implement a matrix completion algorithmic approach
to the recommender problem. To that end it will construct a matrix where the
rows are indexed by joke and columns are indexed by users
"""

import sqlite3 as sql

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_clean_data():
    """
    This function will pull from the sqlite database 'jokedb.sqlite3' data
    related to the joke raters, joke ratings, and jokes themselves.
    It will minimally format the data, removing duplicate entries.

    It will return three DataFrames the first containing information
    regarding the joke raters, the second containing information about the
    joke ratings, and the third containing information about the jokes.

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
