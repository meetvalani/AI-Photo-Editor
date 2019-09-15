from django.shortcuts import render

# Create your views here.
def object_removal(request):
    return render(request,'object_removal.html',{})