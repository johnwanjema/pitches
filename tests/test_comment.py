import unittest
from app.models import User,Comments
from app import db

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_comment = Comments(comment= 'nice pitch')

    def tearDown(self):
        Comments.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'nice pitch')
        self.assertEquals(self.new_comment.User,self.user_James)
    def test_save_pitch(self):
        self.new_Comment.save_Comment()
        self.assertTrue(len(Comments.query.all())>0)

    