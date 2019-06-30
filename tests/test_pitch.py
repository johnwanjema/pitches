import unittest
from app.models import Pitch,User
from app import db

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch = Pitch(pitch_category = 'interview',pitch_title = 'moringa', pitch_upvotes = 0, pitch ='i love business', pitch_downvotes = 0, user = self.user_James)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_category,'interview')
        self.assertEquals(self.new_pitch.pitch_title,'moringa')
        self.assertEquals(self.new_pitch. pitch_upvotes,0)
        self.assertEquals(self.new_pitch.pitch,'i love business')
        self.assertEquals(self.new_pitch.pitch_downvotes,0)
        self.assertEquals(self.new_pitch.User,self.user_James)
        
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    