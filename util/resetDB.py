import sqlite3

open("../data/info.db","w").close() #Resets Database

db = sqlite3.connect("../data/info.db")
c = db.cursor()

#Creates table to store review information
c.execute("CREATE TABLE IF NOT EXISTS reviews(username TEXT, review TEXT, movieName TEXT, rating INTEGER)")

#Creates table to store user information
c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT)")

#Creates table to store comments
c.execute("CREATE TABLE IF NOT EXISTS comments(movieName TEXT, comment TEXT, username TEXT)")

#Creates table to store movies added to a user's profile
c.execute("CREATE TABLE IF NOT EXISTS moviesAdded(username TEXT, movieName TEXT)")

#Creates table to store friends
c.execute("CREATE TABLE IF NOT EXISTS friends(username TEXT, friendName TEXT)")

db.commit()
db.close()
