from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({'info': 'Ecom API', 'name': "Athar Aiman Khan"})
