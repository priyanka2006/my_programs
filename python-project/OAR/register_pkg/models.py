from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from hello import db

class User(db.Model): # backend for user module
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), nullable = False)
	email = db.Column(db.String(100), unique = True, nullable = False)
	password = db.Column(db.String(100), nullable = False)
	posts = db.relationship('Post',backref='author', lazy = True)

	def __repr__(self):
		return f"User('{self.username}','{self.email}')"

class Post(db.Model): # backend for post module
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(20), nullable = False)
	time = db.Column(db.DateTime, default = datetime.utcnow(), nullable = False)
	content = db.Column(db.String(200), nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

	def __repr__(self):
		return f"Post('{self.title}','{self.time}')"