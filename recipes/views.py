from django.shortcuts import render


def home(request):
    # async with AsyncClient() as client:
    #     blaze_response = await client.get("https://blaze-4.com/api/crash_games/history?")
    #     return JsonResponse(json.loads(blaze_response.text))
    return render(request=request, template_name="recipes/home.html", context={"name": "Yago Freire"})

