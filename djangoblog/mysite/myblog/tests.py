from django.test import TestCase
from django.contrib.auth.models import User
from myblog.models import Post

class PostTestCase(TestCase):
    fixtures = ['myblog_test_fixture.jason',]

    def settings(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title for test"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)



# Create your tests here.
