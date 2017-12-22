from  django.http import HttpResponse

# Create your views here.

def home(request):
    html="<h1> this is the new homepage<h1>"
    return HttpResponse(html)
