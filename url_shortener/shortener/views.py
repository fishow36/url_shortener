from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import URL
from .forms import URLForm
import requests
from urllib3.exceptions import HTTPError as BaseHTTPError

CHARACTERS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_long_link_id(short_url):
    res = 0
    for i , letter in enumerate(short_url[::-1]):
        add = CHARACTERS.find(letter)
        res += add * 62**i
    return (res)

def get_short_link(url_id):
    res = ''
    while (url_id > 0):
        remainder = CHARACTERS[url_id % 62]
        res = remainder + res
        url_id = url_id // 62
    return (res)

# Create your views here.
def index(request, *args, **kwargs):
	form = URLForm(request.POST or None)
	context = {
		'form': form,
		'short_url' : None,
		'url_to_show': None
	}
	if request.method == "POST":
		link = request.POST['long_url']
		try:
			response = requests.get(link)
			if response.status_code >= 400:
				return render(request, 'invalid_link.html', {})
			if form.is_valid():
				form.save()
			url_id = URL.objects.filter(long_url=link).latest('id').id
			context['url_to_show'] = request.META['HTTP_HOST'] + '/' + get_short_link(url_id)
			context['short_url'] = '//' + context['url_to_show']
			return render(request, 'index.html', context)
		except:
			return render(request, 'invalid_link.html', {})
		
	
	return render(request, 'index.html', context)

def redirect_link(request, short, *args, **kwargs):
	link_id = get_long_link_id(short)
	try:
		url = URL.objects.get(id=link_id)
		return redirect(url.long_url)
	except URL.DoesNotExist:
		return render(request, 'page_does_not_exist.html', {})
	