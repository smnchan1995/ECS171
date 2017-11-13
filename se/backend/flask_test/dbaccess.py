
def buildJokeRaterModel(db):
	class JokeRater(db.Model):
		__tablename__ = "jokerater"
		id = db.Column(db.Integer, primary_key=True)
		joke_submitter_id = db.Column(db.String)
		gender = db.Column(db.String)
		age = db.Column(db.Integer)
		birth_country = db.Column(db.String)
		major = db.Column(db.String)
		preferred_joke_genre = db.Column(db.String)
		preferred_joke_genre2 = db.Column(db.String)
		preferred_joke_type = db.Column(db.String)
		favorite_music_genre = db.Column(db.String)
		favorite_movie_genre = db.Column(db.String)
	return JokeRater

def buildJokeModel(db):	
	class Joke(db.Model):
		__tablename__ = "joke"
		id = db.Column(db.Integer, primary_key=True)
		category = db.Column(db.String)
		joke_type = db.Column(db.String)
		joke_text = db.Column(db.String)
		joke_submitter_id = db.Column(db.Integer, db.ForeignKey('jokerater.id'))
		joke_source = db.Column(db.String)
	return Joke

def buildJokeRatingModel(db):
	class JokeRating(db.Model):
		__tablename__ = "jokerating"
		id = db.Column(db.Integer, primary_key=True)
		rating = db.Column(db.Integer)
		joke_id = db.Column(db.Integer, db.ForeignKey('joke.id'))
		joke_rater_id = db.Column(db.Integer, db.ForeignKey('jokerater.id'))
	return JokeRating
