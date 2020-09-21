from django.test import TestCase
from django.test import SimpleTestCase
from .models import URL
# Create your tests here.

class URLmodeltests(TestCase):
	
	def test_simple_check(self):
		print("Method: test_one_plus_one_equals_two.")
		self.assertEqual(1 + 1, 2)
	
	def test_main_page(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
	
	def test_wrong_link(self):
		response = self.client.get('/aa98', follow=True)
		SimpleTestCase.assertRedirects(self=self, response=response, 
		expected_url='/aa98/', 
		status_code=301,
		target_status_code=200,
		msg_prefix='',
		fetch_redirect_response=True)
		# self.assertEqual(response.status_code, 301)
	
	def test_redirect(self):
		print(len(URL.objects.all()))
		example_url = 'https://www.google.com'
		URL.objects.create(long_url=example_url)
		response = self.client.get('/1/', follow=True)
		with open ('check.txt', 'w') as f:
			f.write(str(response.request))
			f.write(str(response.content))
			# f.write(str(response.text))
			f.write(str(response.status_code))
		self.assertEqual(response.status_code, 200)
		# SimpleTestCase.assertRedirects(self=self, response=response, 
		# expected_url=example_url, 
		# status_code=301,
		# target_status_code=302,
		# msg_prefix='',
		# fetch_redirect_response=True)