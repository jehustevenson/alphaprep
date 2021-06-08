from flask import Blueprint

tests = Blueprint(
'tests',
__name__,
static_folder = 'static',
template_folder = 'templates',
static_url_path = '/tests'
)
