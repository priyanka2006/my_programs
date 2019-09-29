from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
	return render_template("home.htm", title="home")

@app.route("/about")
def about():
	return render_template("about.htm", title="about")

if __name__=="__main__":
	app.run(debug=True)