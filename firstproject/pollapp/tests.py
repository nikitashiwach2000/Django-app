from django.test import TestCase

# Create your tests here.
import datetime

# from django.test import TestCase
from django.utils import timezone

from .models import questions


class questionsModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = questions(date=timezone.now() + datetime.timedelta(days=30))
        # future_question = questions(date=time)
        self.assertIs(future_question.was_published_recently(), False)
print("test")