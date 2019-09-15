from django.shortcuts import render

# Create your views here.
def image_to_map(request):
    return render(request,'image_to_map.html',{})
