from django.shortcuts import render
from django.http import HttpResponse
from . models import feature

# Create your views here.
def index(request):
    feature1 = feature()
    feature1.id = 0
    feature1.name = 'Socials'
    feature1.details = 'LinkedIn, Facebook'

    
    feature2 = feature()
    feature2.id = 1
    feature2.name = 'Github'
    feature2.details = 'ashwin-adhikari'

    feature3 = feature()
    feature3.id = 2
    feature3.name = 'Challenge'
    feature3.details ='day 3'

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
    # features = [feature1, feature2, feature3]
    # return render(request, 'index.html',{'feature1':feature1, 'feature2': feature2,'feature3' :feature3},)
    #instead of this making list is very fast and efficient

    features = feature.objects.all()
    #each of the value in the database is get by this and passes to index.html
    return render(request, 'index.html',{'features':features},)




def counter(request):
    text = request.POST['text']
    length_of_words = len(text.split())
    return render(request,'counter.html', {'length': length_of_words})