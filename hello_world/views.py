from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(f"Hello, world! Request method: {request.method}")