import twitterAPI
import os


from flask import Flask, render_template, flash, url_for , redirect , config
from form import Submissionform    
from flask_wtf.csrf import CsrfProtect
#csrf = CsrfProtect()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'now-you-see-me'
    
app = Flask(__name__)
app.config.from_object(Config)
#csrf.init_app(app)

@app.route("/", methods=['GET','POST'])           
def home():
	form = Submissionform()
	if form.validate_on_submit():
		flash('Tweet posted successfully! :  {}'.format(form.text.data))
		status = twitterAPI.tweet(form.text.data)
		return redirect(url_for('home'))
	else:
		flash_errors(form)
	return render_template('homepage.html',form=form)
	
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Invalid input in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')   
    
@app.route("/about", methods=['GET','POST'])
def about():
	posts = twitterAPI.get_tweets('Zisyang')
	return render_template('about_page.html',posts=posts,twitterAPI=twitterAPI)

@app.route("/delete", methods=['GET','POST']) 
def delete():
	form = Submissionform()
	if form.validate_on_submit():
		flash('Successfully deleted the tweet with the provided tweet ID :  {}'.format(form.text.data))
		status = twitterAPI.del_tweet(form.text.data)
		return redirect(url_for('delete'))
	else:
		flash_errors(form)
	return render_template('delete_tweet.html',form=form)
    
if __name__ == "__main__":
    app.run(debug=True)
 
