from flask import Blueprint, render_template, request, redirect
from flask_login import current_user

main = Blueprint(
'main',
__name__,
static_folder = 'static',
template_folder = 'templates',
static_url_path = '/main'
)


@main.route("/")
@main.route("/home")
def home():
    return redirect(url_for('main.login'))

@main.route("/about-dev")
def about_dev():
    return render_template('about_dev.html', title = 'About - Developers')


@main.route("/bugs", methods=['GET', 'POST'])
def bugs():
    
    if request.method == 'POST':
        report = request.form['report']
#        dbloader.load_bug_report(report) replace with the normal way of sqlalchemy
        flash("Thank You! Our team will get right on fixing the issues you've reported. :)", 'success')
    return render_template('bugs.html')


@main.route("/mobile-error", methods = ['GET'])
def mobile_response():
    return render_template('mobileresponse.html')
            
@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405

@main.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




