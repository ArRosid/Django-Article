from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This is Home</h1>")

def about_me(request):
    return HttpResponse("<h1>About Me</h1>")