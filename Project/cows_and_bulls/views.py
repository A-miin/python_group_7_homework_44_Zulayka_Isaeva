from django.shortcuts import render
from random import randint
# Create your views here.
numbers=[]
def set_numbers():
    global numbers
    numbers = []
    while True:
        a = randint(1,10)
        if a not in numbers:
            numbers.append(a)
        if len(numbers)==4:
            break

def home(request):
    set_numbers()
    print(numbers)
    return render(request, 'home.html')

def game(request):
    if request.method=="GET":
        return render(request,'game.html')