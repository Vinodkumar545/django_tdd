# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

class HomePageTest(TestCase):

	def test_uses_home_template(self):
		response = self.client.get('/')
		# self.assertTrue(response.content.decode().startswith('<html>'))
		# self.assertIn('<title> To-Do lists </title>', response.content.decode())
		# self.assertTrue(response.content.decode().strip().endswith('</html>'))
		self.assertTemplateUsed(response, 'home.html')

	def test_handles_post_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertIn('A new list item', response.content.decode())
