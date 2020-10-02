from flask import Flask, render_template, request, jsonify,redirect, url_for,Response, session
import requests 
import os
import io
import json
import time
import datetime
import pickle
import random
from redbot import redditbot
import multiprocessing 

app = Flask(__name__)

app.secret_key = '1t_1s_4_5ecre7_c0de'

bot = redditbot()

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == "POST":
		title = request.form['title']
		session['t'] = title
		session['l'] = request.form['link']
		session['s'] = request.form['subreddits']
		print(session)
		return redirect(url_for('followup', t=title))

	else: 
		return render_template('index.html')

@app.route("/<t>")
def followup(t):
	link = session['l']
	try:
		hashcode = list(link.split('?v='))[-1]
		print(hashcode)
	except:
		hashcode = list(link.split('/'))[-1]
		print(hashcode)

	subs = session['s']
	subs = list(subs.split(','))

	p1 = multiprocessing.Process(target=bot.submit, args=(session, )) 
	p1.start()

	return render_template('user.html',hashcode=hashcode, title=session['t'], subs=subs)

	# return render_template('user.html',title=title, link=hashcode, subs=subs)


if __name__ == '__main__':
   app.run(debug = True,use_reloader=False)