# testing_quality_assurance/tests.py
from django.test import TestCase
from .models import YourModel

class YourModelTestCase(TestCase):
    def test_something(self):
        # Example test case
        your_model = YourModel.objects.create(name="Test Item")
        self.assertEqual(your_model.name, "Test Item")
