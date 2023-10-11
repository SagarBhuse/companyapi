from django.http  import  HttpResponse, JsonResponse
def home_page(request):
    print("Home Page requested")
    friends=[
        'harshada',
        'sagar',
        'tanmay'
    ]
    return JsonResponse(friends,safe=False)