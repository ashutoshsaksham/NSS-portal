from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpRequest

from portal.models import Ngo, Activity


# Create your views here.
def index(request):
    return render(request, './portal/homepage.html')


def activity(request, ngo_id):
    actvty = Activity.objects.filter(ngos_activity_id = ngo_id)
    print(actvty)
    params = {'activity_name' : actvty,
              'ngo_name' : Ngo.ngo_name}
    return render(request, 'portal/activity.html',params)
    


def about(request):
    return HttpRequest(request, "we are at about")

def ngologin(request):
    return render (request, 'portal/ngologin.html')

def contact(request):
    return HttpRequest(request, "we are at contact")


def ngos(request):
    ngos = Ngo.objects.all()
    print(ngos)
    params = {'ngo_no' : ngos}
    return render(request, 'portal/ngos.html',params)



