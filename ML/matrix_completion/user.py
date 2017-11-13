"""
user.py

This should include basic information about users
"""
from matrix_complete import read_clean_data

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
    return [field.prompt() for field in all_user_fields]
