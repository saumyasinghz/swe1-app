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
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
