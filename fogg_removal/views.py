from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fogg_removal(request):
    #return HttpResponse("<h1>working fogg_removal</h1>")
    return render(request,'fogg_removal.html',{})