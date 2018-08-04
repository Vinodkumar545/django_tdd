# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# def test_smoke_test():
# 	assert 1+1 = 3

class HomePageTest(TestCase):

	def test_uses_home_template(self):
		reponse = self.client.get('/')
		self.assertTrue(reponse.content.decode().startswith('<html>'))
		self.assertIn('<title> To-Do lists </title>', reponse.content.decode())
		self.assertTrue(reponse.content.decode().strip().endswith('</html>'))
		self.assertTemplateUsed(reponse, 'home.html')

	def test_handles_post_request(self):
		
