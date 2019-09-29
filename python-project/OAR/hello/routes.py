from flask import Flask,render_template, url_for,flash,redirect
from hello.forms import RegisterForm, LoginForm
from hello import app,db
from hello.models import User, Post


@app.route("/login", methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# to access email from data base
		user = User.query.filter_by(email=form.email.data).first()
		#to compair email and password stored in database
		if user and form.password.data == user.password:
			flash(f'You are successfully login', 'success')
			return redirect(url_for('contactus'))
		else:
			flash(f'Register your details first', 'danger')
			return redirect(url_for('register'))
	return render_template("login.html", title="login", form = form)


@app.route("/register", methods = ['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		#to store data into data base
		user = User(username=form.username.data, email=form.email.data, password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Your Account Created! You can login', 'success')
		return redirect(url_for('login'))
	return render_template("register.html", title="register", form = form)


@app.route("/contactus")
def contactus():
	return render_template("contactus.html", title="contactus")

