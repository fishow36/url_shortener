from django.test import TestCase, Client
from django.test import SimpleTestCase
from .models import URL
from django.http import HttpResponse
import requests
# Create your tests here.

class URLmodeltests(TestCase):
	
	def setUp(self):
		URL.objects.create(long_url='https://www.google.com')
		URL.objects.create(long_url='https://github.com/avito-tech/auto-backend-trainee-assignment')
		URL.objects.create(long_url='https://www.youtube.com/watch?v=QF4ZF857m44&t=2753s')
		URL.objects.create(long_url='https://twitter.com/home')
		URL.objects.create(long_url='https://vk.com/')
		URL.objects.create(long_url='https://glosbe.com/')
		URL.objects.create(long_url='https://mail.ru/')
		URL.objects.create(long_url='https://translate.google.ru/')
		URL.objects.create(long_url='https://21-school.ru/onlineeducation')
		URL.objects.create(long_url='https://vk.com/fishowl')
		print("10 URLs added.")
	
	def test_main_page(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		print("main page returned 200")
	
	def test_wrong_link_wrong_object(self):
		response = self.client.get('/aa98', follow=True)
		SimpleTestCase.assertRedirects(self=self, response=response, 
		expected_url='/aa98/', 
		status_code=301,
		target_status_code=404,
		msg_prefix='',
		fetch_redirect_response=True)
		print("wrong link '/aa98' returned 404")
	
	def test_wrong_link_wrong_page_with_dot(self):
		response = self.client.get('/4.22')
		self.assertEqual(response.status_code, 404)
		print("wrong link '/4.22' returned 404")

	def test_wrong_link_wrong_page_many_slashes(self):
		response = self.client.get('/a/b/c/')
		self.assertEqual(response.status_code, 404)
		print("wrong link '/a/b/c/' returned 404")
	
	def test_get_object(self):
		obj = URL.objects.get(id=1)
		self.assertEqual(obj.long_url, 'https://www.google.com')
		print("1st object is https://www.google.com")

	def test_correct_link(self):
		client = Client()
		response = self.client.get('/5', follow=True)
		self.assertEqual(response.status_code, 200)
		print(f'link /5 returned status code 200')