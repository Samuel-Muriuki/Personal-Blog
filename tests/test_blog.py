from app.models import Comment,User,Blog
from app import db
from app import app
import unittest

class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Samm = User(username = 'Samm',password = 'Vanilla', email = 'test@gmail.com')
        self.new_blog = Blog(id=1,title_blog='Test',blog_content='This is a test blog',category="interview",user = self.user_Samm)

    def tearDown(self):
        User.query.delete()
        Blog.query.delete()
        Comment.query.delete()
      

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title_blog,'Test')
        self.assertEquals(self.new_blog.blog_content,'This is a test blog')
        self.assertEquals(self.new_blog.category,"interview")
        self.assertEquals(self.new_blog.
        user,self.user_Peris)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        got_blog= Blog.get_blog(1)
        self.assertTrue(got_blog is not None)
