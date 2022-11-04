from django.shortcuts import render
from .models import RuralInfraAwcAcEnglishconverted
# Create your views here.
def homePage(request):
    return render(request, 'viewHome.html')
def viewMap(request):
    awc = RuralInfraAwcAcEnglishconverted.objects.filter(agan_type='मुख्य',project='Yavatmal')
    context = {'awc': awc}
    return render(request,'viewMap.html',context)
    # return render(request, 'viewMap.html')

def aboutUs(request):
    return render(request, 'viewMap.html')

def map_query(request):
    awc_rur_infra = RuralInfraAwcAcEnglishconverted.objects.all()
    context = {'awc_rural_infra': awc_rur_infra}
    return render(request,viewMap.html,context)