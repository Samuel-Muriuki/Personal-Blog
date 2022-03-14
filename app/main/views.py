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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    # pitch_count = Pitch.pitch_number(uname)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
