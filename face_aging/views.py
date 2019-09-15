from django.shortcuts import render

# Create your views here.
def face_aging(request):
    return render(request,'face_aging.html',{})