from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def game(request):
    if request.method=="GET":
        return render(request,'game.html')