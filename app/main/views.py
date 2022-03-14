from flask import render_template,request,redirect,url_for,abort, flash, jsonify
from . import main
from .forms import BlogForm,UpdateProfile, CommentForm
from ..models import User,Blog,Comment
from flask_login import login_required, current_user
from .. import db,photos
from ..request import get_blogs


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The Blogging Website'
    blogs = get_blogs()

    return render_template('index.html',title = title,blogs = blogs)