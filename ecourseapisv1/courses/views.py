
from django.http import HttpResponse

# Create your views here.
# It is Controller

def index(request):
    return HttpResponse('Hello, World!!')