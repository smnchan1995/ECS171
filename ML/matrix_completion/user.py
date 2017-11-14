"""
user.py

This should include basic information about users
"""

import sqlite3 as sql

import pandas as pd

from forms import IntegerField, CategoricalField

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

joke_raters, _, _ = read_clean_data()

gender_field = CategoricalField('gender', joke_raters['gender'].unique())
age_field = IntegerField('age', 0, 120)
birth_country_field = CategoricalField(
    'birth country', joke_raters['birth_country'].unique())
major_field = CategoricalField('major', joke_raters['major'].unique())
joke_genre_field = CategoricalField('joke genre',
    joke_raters['preferred_joke_genre'].unique())
joke_type_field = CategoricalField('joke type',
    joke_raters['preferred_joke_type'].unique())
music_genre_field = CategoricalField("Favorite Music Genre",
    joke_raters['favorite_music_genre'].unique())
movie_genre_field = CategoricalField("Favorite Movie Genre",
    joke_raters['favorite_movie_genre'].unique())

all_user_fields = [
    gender_field,
    age_field,
    birth_country_field,
    major_field,
    joke_genre_field,
    joke_genre_field, # Twice because we have two preferred genre fields
    joke_type_field,
    music_genre_field,
    movie_genre_field
]


def read_user():
    """
    This function will prompt the user for input about all the user
    parameterizations.
    """
    return [field.read_input() for field in all_user_fields]
