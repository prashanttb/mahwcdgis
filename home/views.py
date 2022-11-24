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
        # angan_type = request.POST.get('agan_type')
        # constr = request.POST.get('constr')
        # sitangan = request.POST.get('sitangan')
        cate1 = request.POST.get('cate1')
        cate2 = request.POST.get('cate2')
        cate3 = request.POST.get('cate3')
        
        cate_val1 = request.POST.get('cate_val1')
        cate_val2 = request.POST.get('cate_val2')
        cate_val3 = request.POST.get('cate_val3')
        
        #print(cate2)
         
        filters = {}
        if dist!="Select District":
            filters['district'] = dist
        if taluka!="Select Taluka":
            filters['block_n'] = taluka
        if cate1!="" and cate_val1!="":
            filters[cate1]=cate_val1
        if cate2!="" and cate_val2!="":
            filters[cate2]=cate_val2
        if cate3!="" and cate_val3!="":
            filters[cate3]=cate_val3
        # if angan_type!="":
        #     filters['agan_type'] = angan_type
        # if constr!="":
        #     filters['agancbuil_field'] = constr
        # if sitangan!="":
        #     filters['child_sitagan'] = sitangan

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

def about_wwd(request):
    return render(request, 'about_wwd.html')

def about_op(request):
    return render(request, 'about_op.html')

def about_p(request):
    return render(request, 'about_p.html')

def map_query(request):
    awc_rur_infra = RuralInfraAwcAcEnglishconverted.objects.all()
    context = {'awc_rural_infra': awc_rur_infra}
    return render(request,viewMap.html,context)

@csrf_exempt
def category(request):
    if request.method == "POST":
        cate1 = request.POST.get('category_1')
        cate2 = request.POST.get('category_2')
        cate3 = request.POST.get('category_3')
        
        d1=""
        d2=""
        d3=""
        if cate1!="":
            d1 = list(RuralInfraAwcAcEnglishconverted.objects.values(cate1).order_by(cate1).distinct())
        if cate2!="":
            d2 = list(RuralInfraAwcAcEnglishconverted.objects.values(cate2).order_by(cate2).distinct())
        if cate3!="":
            d3 = list(RuralInfraAwcAcEnglishconverted.objects.values(cate3).order_by(cate3).distinct())    
            
        #print(d1)
        context = {'c1':d1,'c2':d2,'c3':d3}
        
        return JsonResponse(context)
        #return render(request,'viewMap.html')
