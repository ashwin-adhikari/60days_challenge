from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # name = 'John'
    # context = {
    #     'name': 'Sam',
    #     'age': 22,
    #     'country': 'Nepal'
    # }
    #this name might come from database, everytime we login we give our name 
    # return HttpResponse('<h1> Hey, welcome</h1>')
    # return render(request, 'index.html',{'name':name})
    # return render(request, 'index.html',context)
    return render(request, 'index.html')
def counter(request):
    text = request.GET['text']
    length_of_words = len(text.split())
    return render(request,'counter.html', {'length': length_of_words})