from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    context = {
        'title':'Project Management',
    }
    template = loader.get_template('home.html')
    return render(request, 'home.html', context)
    # return HttpResponse('<h1> Project Management Screen Successful</h1>')
    