from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import current_user
from app.decorators import check_confirmed

tutorials = Blueprint(
'tutorials',
__name__,
static_folder = 'static',
template_folder = 'templates',
static_url_path = '/tutorials'
)



@check_confirmed  
@tutorials.route('/tutorialslanding', methods = ['GET', 'POST'])
def tutorials_landing():
    if current_user.is_anonymous:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('main.login'))
    return render_template('tutorialslanding_final.html', title = 'Tutorials Landing Page')

 
@check_confirmed  
@tutorials.route('/englishlanding', methods = ['GET', 'POST'])
def english_landing():
    if current_user.is_anonymous:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('main.login'))
    return render_template('english_landing.html', title = 'Tutorials Landing Page')

 
@check_confirmed  
@tutorials.route('/intsciencelanding', methods = ['GET', 'POST'])
def intscience_landing():
    if current_user.is_anonymous:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('main.login'))
    return render_template('sciencelanding.html', title = 'Tutorials Landing Page')
    

@check_confirmed  
@tutorials.route('/cmathlanding', methods = ['GET', 'POST'])
def cmath_landing():
    if current_user.is_anonymous:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('main.login'))
    return render_template('cmathlanding.html', title = 'Core Math Tutorials')



@check_confirmed  
@tutorials.route('/sociallanding', methods = ['GET', 'POST'])
def social_landing():
    if current_user.is_anonymous:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('main.login'))
    return render_template('sociallanding.html', title = 'Tutorials Landing Page')



@check_confirmed   
@tutorials.route('/tutorials', methods = ['GET', 'POST'])
def tutorial():
    return "Tutorials"
#    subject = request.form['subject']
#    topic = request.form['topic']
#    
#    
#    videos = dbloader.load_videos(subject, topic)
#    pdfs = dbloader.load_pdfs(subject, topic)    
#    
#    return render_template('tutorials_final.html',topic=topic,videos=videos, pdfs=pdfs,  title = 'Tutorials Page')


@tutorials.route('/return-file/', methods =['GET','POST'])
def return_file(): # to be able download the pdfs
    main = 'pdffiles/'
    file = request.form['file']
    
    file_path = main + file
    # the send_file function is in flask and aids us to download the pdf
    
    return send_file(file_path, attachment_filename = 'Tutorials.pdf')