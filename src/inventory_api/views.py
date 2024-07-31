from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import API

@csrf_exempt
def register(request):
    if request.method == "POST":
        product = [request.POST.get("id"),request.POST.get("name"),request.POST.get("sellprice"),request.POST.get("purchaseprice"),request.POST.get("link")]
        if None in product:
            return HttpResponse("404")
        
        product[2] = API.strToNumber(product[2])
        product[3] = API.strToNumber(product[3])

        if False in product:
            print("Not number")
            return HttpResponse(False)
        
        products,log = API.load()
        return HttpResponse(API.register_product(products,log,product[0],product[1],product[2],product[3],product[4]))
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

@csrf_exempt
def remove(request):
    if request.method == "POST":
        id = request.POST.get("id")
        payment = request.POST.get("payment")
        if id is None or payment is None:
            return HttpResponse("404")
        
        products,log = API.load()
        return HttpResponse(API.remove_product(products,log,id,payment))
    return HttpResponse("404")

@csrf_exempt
def delete(request):
    if request.method == "POST":
        id = request.POST.get("id")
        if id is None :
            return HttpResponse("404")
        
        products,log = API.load()
        return HttpResponse(API.delete_product(products,log,id))
    return HttpResponse("404")

@csrf_exempt
def get(request):
    if request.method == "POST":
        id = request.POST.get("id")
        if id is None :
            return HttpResponse("404")
        
        products,log = API.load()
        return JsonResponse({"response": API.get_product(products,id)})
    return HttpResponse("404")

@csrf_exempt
def modify(request):
    if request.method == "POST":
        product = [request.POST.get("id"),request.POST.get("name"),request.POST.get("nb"),request.POST.get("sellprice"),request.POST.get("purchaseprice"),request.POST.get("link")]
        if None in product:
            return HttpResponse("404")
        
        product[2] = API.strToNumber(product[2])
        product[3] = API.strToNumber(product[3])
        product[4] = API.strToNumber(product[4])

        if False in product:
            print("Not number")
            return HttpResponse(False)
        
        products,log = API.load()
        return HttpResponse(API.modify_product(products,log,product[0],product[1],product[2],product[3],product[4],product[5]))
    return HttpResponse("404")

def list_(request):
    products,log = API.load()
    return JsonResponse(products);