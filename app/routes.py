from flask import render_template, url_for, flash, redirect, request, send_file, session
from alphaprep import app, db, bcrypt, mail
from alphaprep.models import User
from flask_mail import Message
from datetime import datetime, timedelta


# this function is for sending messages to the user when they have been off for a while
def msg(user):
    if today.day - user.user_streak[-1].last_login.day % 4 == 0 and today.day - user.user_streak[-1].last_login.day < 40 :
        message = f'''It's been a while since we have heared from you! 
    It's never too bad a time to keep studying. Why not come take a test with us?
    
    {url_for('users.login', _external=True)}'''

with app.app_context():
    with mail.connect() as conn: # setting up mail connection
        today = datetime.now() # getting today's time
        users = User.query.all() # gets all users
        filter(lambda user: msg(user), users)
         # the link sent is to the login page and this is the body of the message
    subject = "hello! We miss you! %s" % user.username
    msg = Message(recipients=[user.email],
     body=message,
                              subject=subject, sender=('Alpha Prep', 'noreply@sender.com'))

    conn.send(msg)#sends the message
				
				
			
