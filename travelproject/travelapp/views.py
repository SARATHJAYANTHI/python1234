from django.shortcuts import render

# Create your views here.
from travelapp.models import  Place1


def demo(request):
    obj2=Place1.objects.all()
    return render(request,"index.html",{'res':obj2})