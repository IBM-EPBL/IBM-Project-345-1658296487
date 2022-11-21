from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import datetime
import pickle
import database as db


app = Flask(__name__, template_folder="template")
model = pickle.load(open("./models/cat.pkl", "rb"))
print("Model Loaded")

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")


@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
	if request.method == "POST":
		# DATE
		date = request.form['date']
		day = float(pd.to_datetime(date, format="%Y-%m-%dT").day)
		month = float(pd.to_datetime(date, format="%Y-%m-%dT").month)
		# MinTemp
		minTemp = float(request.form['mintemp'])
		# MaxTemp
		maxTemp = float(request.form['maxtemp'])
		# Rainfall
		rainfall = float(request.form['rainfall'])
		# Evaporation
		evaporation = float(request.form['evaporation'])
		# Sunshine
		sunshine = float(request.form['sunshine'])
		# Wind Gust Speed
		windGustSpeed = float(request.form['windgustspeed'])
		# Wind Speed 9am
		windSpeed9am = float(request.form['windspeed9am'])
		# Wind Speed 3pm
		windSpeed3pm = float(request.form['windspeed3pm'])
		# Humidity 9am
		humidity9am = float(request.form['humidity9am'])
		# Humidity 3pm
		humidity3pm = float(request.form['humidity3pm'])
		# Pressure 9am
		pressure9am = float(request.form['pressure9am'])
		# Pressure 3pm
		pressure3pm = float(request.form['pressure3pm'])
		# Temperature 9am
		temp9am = float(request.form['temp9am'])
		# Temperature 3pm
		temp3pm = float(request.form['temp3pm'])
		# Cloud 9am
		cloud9am = float(request.form['cloud9am'])
		# Cloud 3pm
		cloud3pm = float(request.form['cloud3pm'])
		# location
		location = float(request.form['location'])
		# Wind Dir 9am
		winddDir9am = float(request.form['winddir9am'])
		# Wind Dir 3pm
		winddDir3pm = float(request.form['winddir3pm'])
		# Wind Gust Dir
		windGustDir = float(request.form['windgustdir'])
		# Rain Today
		rainToday = float(request.form['raintoday'])

		input_lst = [location , minTemp , maxTemp , rainfall , evaporation , sunshine ,
					 windGustDir , windGustSpeed , winddDir9am , winddDir3pm , windSpeed9am , windSpeed3pm ,
					 humidity9am , humidity3pm , pressure9am , pressure3pm , cloud9am , cloud3pm , temp9am , temp3pm ,
					 rainToday , month , day]
		pred = model.predict(input_lst)
		output = pred
		if output == 0:
			return render_template("after_sunny.html")
		else:
			return render_template("after_rainy.html")
	return render_template("predictor.html")

@app.route("/Login",methods=['GET', 'POST'])
def Login():
	return render_template("Login.html",status="")

@app.route("/result", methods=['POST','GET'])
def result():
	if request.method == 'POST':
		email = str(request.form['email'])
		password = str(request.form['pwd'])
		if len(email)<=40 and len(password)<=30:
			if db.login(email,password):
				return render_template("predictor.html")
			else:
				return render_template("Login.html",status="Invalid data")

@app.route("/Registration",methods=['GET', 'POST'])
def Registration():
	return render_template("Registration.html",status="")

@app.route("/Registrte",methods=['GET', 'POST'])
def Registrate():
	if request.method == 'POST':
		username = str(request.form['username'])
		email = str(request.form['email'])
		password = str(request.form['pwd'])
		if len(username)<25 and len(email)<40 and len(password)<30:
			if db.registration(username,email,password):
				return render_template("predictor.html")
		else:
			return render_template("Registration.html",status="Invalid data")

@app.route("/Feedback",methods=['GET', 'POST'])
def Feedback():
	return render_template("Feedback.html")


@app.route("/submit",methods=['GET', 'POST'])
def submit():
	if request.method == 'POST':
		username = str(request.form['username'])
		email = str(request.form['email'])
		phone_number = str(request.form['ph'])
		message = str(request.form['msg'])
		if len(username)<=25 and len(email)<=40 and len(phone_number)<=15 and len(message)<=250:
			if db.feedback(username,email,phone_number,message):
				return render_template("index.html")
		else:
			return render_template("predictor.html")


if __name__=='__main__':
	app.run(debug=True)
