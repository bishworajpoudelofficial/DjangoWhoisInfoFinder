# app views.py
from django.shortcuts import render
import whois  # Make sure you're using the correct library

def index(request):
    return render(request, 'whoisapp/index.html')

def details(request):
    # Get domain name from the form
    domain = request.GET.get('domain')
    info = {}

    # Try to retrieve WHOIS information
    try:
        info = whois.whois(domain)
    except Exception as e:
        info = {'error': str(e)}

    return render(request, 'whoisapp/details.html', {'domain': domain, 'info': info})
