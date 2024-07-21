from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import API

@csrf_exempt
def register(request):
    if request.method == "POST":
        product = [request.POST.get("id"),request.POST.get("name"),request.POST.get("sellprice"),request.POST.get("purchaseprice")]
        if None in product:
            return HttpResponse("404")
        
        products,log = API.load()
        return HttpResponse(API.register_product(products,log,product[0],product[1],product[2],product[3]))
    return HttpResponse("404")

@csrf_exempt
def add(request):
    if request.method == "POST":
        id = request.POST.get("id")
        if id is None:
            return HttpResponse("404")
        
        products,log = API.load()
        return HttpResponse(API.add_product(products,log,id))
    return HttpResponse("404")