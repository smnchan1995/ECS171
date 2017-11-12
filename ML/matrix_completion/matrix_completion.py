#Andy Tran 11/11/17
import sqlite3 as sql
import pandas as pd

def readCleanData():
    jokedb = sql.connect("jokedb.sqlite3")
    JokeRater = pd.read_sql_query("SELECT * from JokeRater", jokedb)
    Joke = pd.read_sql_query("SELECT * from Joke", jokedb)
    JokeRating = pd.read_sql_query("SELECT * from JokeRating", jokedb)

    JokeRater = JokeRater.drop(['joke_submitter_id'], axis = 1).set_index('id')
    #JokeRater['age'] = st.norm.cdf((JokeRater['age'] - JokeRater['age'].mean())/JokeRater['age'].std(ddof=0))
    #JokeRater['preferred_jokes'] = JokeRater['preferred_joke_genre'].map(str) + JokeRater['preferred_joke_genre2']

    Joke = Joke.set_index('id')
    JokeRating = JokeRating.drop_duplicates(['joke_id', 'joke_rater_id'], keep = 'first')
    JokeRating = JokeRating.pivot(index = 'joke_id', columns = 'joke_rater_id', values = 'rating').transpose().fillna(2.5)
    return JokeRater, JokeRating, Joke


[rater, rating, joke] = readCleanData()
print(joke.iloc[105])
#print(rating.columns.get_values())
print(rating.shape)
