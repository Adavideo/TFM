from django.test import TestCase
from .models import Thread


class TheadTests(TestCase):

    def test_create_thread(self):
        thread = Thread(number=1)
        thread.save()
        self.assertIs(thread.number, 1)
        self.assertEqual(str(thread), "Thread number 1")

    def test_update_thread(self):
        thread = Thread(number=1)
        thread.update(title="Title", uri="blabla")
        self.assertIs(thread.title, "Title")
        self.assertIs(thread.uri, "blabla")
        self.assertEqual(str(thread), "Thread number 1 - title: Title")
