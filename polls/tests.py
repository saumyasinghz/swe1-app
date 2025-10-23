from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Question

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


# Create your tests here.


class SmokeTest(TestCase):
    def test_homepage_loads(self):
        """Simple test to ensure the homepage returns 200."""
        response = self.client.get(reverse("polls:IndexView"))
        self.assertEqual(response.status_code, 200)


class QuestionModelTests(TestCase):
    def test_future_question_returns_false(self):
        """
        Questions with a future publication date should return False for was_published_recently().
        """
        future_question = create_question(question_text="Future question.", days=30)
        self.assertIs(future_question.was_published_recently(), False)

    def test_old_question_returns_false(self):
        """
        Questions with a publication date older than 1 day should return False for was_published_recently().
        """
        old_question = create_question(question_text="Old question.", days=-1)
        self.assertIs(old_question.was_published_recently(), False)

    def test_recent_question_returns_true(self):
        """
        Questions with a publication date within the last day should return True for was_published_recently().
        """
        recent_question = create_question(question_text="Recent question.", days=-0.5)
        self.assertIs(recent_question.was_published_recently(), True)
