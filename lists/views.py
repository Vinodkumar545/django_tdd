# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	# pass
	# return HttpResponse('<html> <title> To-Do lists </title> </html>')
	# return render(request, 'home.html')
	if request.method == 'POST':
		return render(request, 'home.html', {'new_item_text': request.POST['item_text']})
	return render(request, 'home.html')
