import sqlite3 as sql
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy.spatial.distance import pdist, squareform
from sklearn import manifold


def readCleanData():
    jokedb = sql.connect("jokedb.sqlite3")
    JokeRater = pd.read_sql_query("SELECT * from JokeRater", jokedb)
    Joke = pd.read_sql_query("SELECT * from Joke", jokedb)
    JokeRating = pd.read_sql_query("SELECT * from JokeRating", jokedb)
    
    JokeRater = JokeRater.drop(['joke_submitter_id'], axis = 1).set_index('id')
    JokeRating = JokeRating.drop_duplicates(['joke_id', 'joke_rater_id'], keep = 'first')
    JokeRating = JokeRating.pivot(index = 'joke_id', columns = 'joke_rater_id', values = 'rating').transpose().fillna(0)
    return JokeRater, JokeRating, Joke

def getEuclideanDistance(JokeRating):
    dist = pdist(JokeRating, 'euclidean')
    df_dist = pd.DataFrame(squareform(dist), index = JokeRating.index, columns = JokeRating.index)
    return df_dist

def distance_map(data):
    '''
    this function takes in a distance matrix and the clusters and outputs a plot
    inputs: data: a SQUARE distance matrix
            cluster: the cluster that each index belongs to, in a DataFrame or list
    
    outputs: a distance plot that color-codes clusters, for up to 9 clusters (more can be added if needed)
    '''
    #http://baoilleach.blogspot.com/2014/01/convert-distance-matrix-to-2d.html
    adist = np.array(data)
    amax = np.amax(adist)
    adist /= amax
    mds = manifold.MDS(n_components=2, dissimilarity="precomputed")
    results = mds.fit(adist)
    coords = pd.DataFrame(results.embedding_, index = data.index)
    #http://stackoverflow.com/questions/26139423/plot-different-color-for-different-categorical-levels-using-matplotlib
    plt.scatter(coords[0], coords[1], marker = 'o')
    plt.title('2D Representation of Distance Matrix')
    plt.show()
 
def userInput():
    #just for now, ideally we need drop down menus
    gender = input('What is your gender? ').strip()
    age = input('What is your age? ').strip()
    birth_country = input('What is your birth country? ').strip()
    major = input('What is your major? ').strip()
    joke_genre1 = input('What is your primary preferred joke genre? ').strip()
    joke_genre2 = input('What is your secondary preferred joke genre? ').strip()
    joke_type = input('What is your preferred joke type? ').strip()
    music_genre = input('What is your favorite music genre? ').strip()
    movie_genre = input('What is your favorite movie genre? ').strip()
    return [gender, age, birth_country, major, joke_genre1, joke_genre2, joke_type,
            music_genre, movie_genre]
    
def raterSimilarity(JokeRater, someGuy):
    similarity = []
    for i in JokeRater.index:
        k = 0
        sim = 0
        for j in JokeRater.loc[i]:
            if j == someGuy[k]:
                sim = sim + 1
            k = k + 1
        similarity.append(sim)
        
    return similarity
            
    
def main():
    someGuy = userInput()
    JokeRater, JokeRating, Joke = readCleanData()
    df_dist = getEuclideanDistance(JokeRating)
    similarity = raterSimilarity(JokeRater, someGuy)
    print(similarity)
    #distance_map(df_dist)
    

if __name__ == "__main__": main()