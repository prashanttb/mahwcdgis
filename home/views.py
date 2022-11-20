from django.shortcuts import render
from .models import RuralInfraAwcAcEnglishconverted
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def homePage(request):
    return render(request, 'viewHome.html')

@csrf_exempt
def viewMap(request):
    if request.method == "POST":
        dist = request.POST.get('district')
        taluka = request.POST.get('taluka')
        angan_type = request.POST.get('agan_type')
        constr = request.POST.get('constr')
        sitangan = request.POST.get('sitangan')
        
        filters = {}
        if dist!="Select District":
            filters['district'] = dist
        if taluka!="Select Taluka":
            filters['block_n'] = taluka
        if angan_type!="":
            filters['agan_type'] = angan_type
        if constr!="":
            filters['agancbuil_field'] = constr
        if sitangan!="":
            filters['child_sitagan'] = sitangan

        print(filters)
        
        district =RuralInfraAwcAcEnglishconverted.objects.filter(**filters)
        # district = RuralInfraAwcAcEnglishconverted.objects.filter(district='')
        district = serializers.serialize('json', district)
        context={"data":district}
        return JsonResponse(context)
    
    else:
        awc = RuralInfraAwcAcEnglishconverted.objects.filter(agan_type='मुख्य',project='Yavatmal')
        # print(awc)
        district = RuralInfraAwcAcEnglishconverted.objects.values('district').order_by('district').distinct()
        taluka = RuralInfraAwcAcEnglishconverted.objects.values('block_n').order_by('block_n').distinct()
        context = {'awc': awc, 'district':district,'taluka':taluka}
        return render(request,'viewMap.html',context)
        # return render(request, 'viewMap.html')

def aboutUs(request):
    return render(request, 'viewMap.html')

def map_query(request):
    awc_rur_infra = RuralInfraAwcAcEnglishconverted.objects.all()
    context = {'awc_rural_infra': awc_rur_infra}
    return render(request,viewMap.html,context)
