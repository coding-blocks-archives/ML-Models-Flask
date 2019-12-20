from flask import Flask, render_template, request
from sklearn.externals import joblib

app = Flask(__name__)


model = joblib.load("model.pkl")

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def main():
	if request.method == 'POST':
		num = float(request.form['number'])
		marks = model.predict([[num]])
	return render_template("index.html", marks = marks)


if __name__ == '__main__':
	app.run(debug = True)