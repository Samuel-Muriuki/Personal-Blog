from app.models import Comment,User,Blog
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Samm = User(username = 'Samm',password = 'Vanilla', email = 'test@gmail.com')
        self.new_blog = Blog(id=1,title_blog='Test',blog_content='This is a test',user = self.user_Samm)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_Samm,blog=self.new_blog)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_Samm)
        self.assertEquals(self.new_comment.blog,self.new_blog)

