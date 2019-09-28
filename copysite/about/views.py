from django.shortcuts import render

# Create your views here.
def new1(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')