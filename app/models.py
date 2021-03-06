
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index =True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(5000))
    profile_pic_path = db.Column(db.String)
    password_hash = db.Column(db.String(255))

    blog = db.relationship('Blog',backref = 'user',lazy = "dynamic")

    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer,primary_key = True)
    title_blog = db.Column(db.String)
    blog_content = db.Column(db.String(1000))
    category = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls,category):
        blog = Blog.query.filter_by(category=category).all()
        return blog

    @classmethod
    def get_blog(cls,id):
        blog = Blog.query.filter_by(id = id).first()

        return blog

    @classmethod
    def get_all_blogs(cls):
        blog = Blog.query.order_by('-id').all()
        return blog
    def __repr__(self):
        return f'Blog {self.blog_content}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(500))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id", ondelete= 'CASCADE'))
    blog_id = db.Column(db.Integer,db.ForeignKey("blog.id", ondelete= 'CASCADE'))
    blog = db.Column(db.Integer,db.ForeignKey("blog.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        

    @classmethod
    def get_comments(cls,blog):
        comments = Comment.query.filter_by(blog_id=blog).all()
        return comments
    
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()
        
    def __repr__(self):
        return f'Comments: {self.comment}'