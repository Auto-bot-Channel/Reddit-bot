import praw
import time
import pickle

class redditbot():
	def __init__(self):

		self.reddit = praw.Reddit(
		    client_id="YOUR_CLIENT_ID", #length=14
		    client_secret="YOIR_CLIENT_SECRET", #lenght=27
		    user_agent="<name> by /u/<username>", #fill in name nd username in same fashion
		    username="YOUR_USERNAMAE",
		    password="YOUR_PASSWORD"
		)
		print(self.reddit.read_only)  # Output: False
		print(self.reddit.user.me())  # your username

	def submit(self,session):

		subreddits,link,title = session['s'], session['l'], session['t']
		
		subreddits = list(subreddits.split(','))
		print('bot posting start!!')

		# post stuff
		self.reddit.validate_on_submit = True
		for subred in subreddits:
			self.reddit.subreddit(subred).submit(title=title, url=link)
			time.sleep(0.1)

		time.sleep(1)