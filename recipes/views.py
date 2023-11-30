from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from httpx import get
# from httpx import AsyncClient
# import json
# Create your views here.


def home(request):
    # async with AsyncClient() as client:
    #     blaze_response = await client.get("https://blaze-4.com/api/crash_games/history?")
    #     return JsonResponse(json.loads(blaze_response.text))
    return render(request=request, template_name="global/home.html")


def contato(request):
    return HttpResponse("CONTATO")


def sobre(request):

    return HttpResponse("SOBRE")
