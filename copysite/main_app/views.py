from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_app1(request):
    return render(request, 'index.html')


def net_gh(request):
    return render(request, 'new.html')

def treni(request):
    return render(request, 'treni.html')