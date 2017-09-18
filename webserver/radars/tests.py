from django.test import TestCase, Client


# Create your tests here.
class FirstTest(TestCase):

    def test_render_page(self):
        client = Client()
        response = client.get('/radars/')
        print(response.content)
        self.assertEqual(response.content, b"Hello, world. You're at the radars index.")