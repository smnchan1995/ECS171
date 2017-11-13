from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JokeRater(Base):
	__tablename__ = "jokerater"
	id = Column(Integer, primary_key=True)
	joke_submitter_id = Column(String)
	gender = Column(String)
	age = Column(Integer)
	birth_country = Column(String)
	major = Column(String)
	preferred_joke_genre = Column(String)
	preferred_joke_genre2 = Column(String)
	preferred_joke_type = Column(String)
	favorite_music_genre = Column(String)
	favorite_movie_genre = Column(String)
	
class Joke(Base):
	__tablename__ = "joke"
	id = Column(Integer, primary_key=True)
	category = Column(String)
	joke_type = Column(String)
	joke_text = Column(String)
	joke_submitter_id = Column(Integer, ForeignKey('jokerater.id'))
	joke_source = Column(String)

class JokeRating(Base):
	__tablename__ = "jokerating"
	id = Column(Integer, primary_key=True)
	rating = Column(Integer)
	joke_id = Column(Integer, ForeignKey('joke.id'))
	joke_rater_id = Column(Integer, ForeignKey('jokerater.id'))
