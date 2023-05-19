from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Fresh Tea"
    return render(request, 'temp/cafe/index.html', {"title": title})

def about(request):
    return render(request, 'temp/cafe/about.html')