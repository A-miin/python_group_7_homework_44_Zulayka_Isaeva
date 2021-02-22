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
    elif request.method =="POST":
        user_nums = []
        cows = 0
        bulls = 0
        for i in range(1,5):
            if int(request.POST.get(f'number{i}')) in user_nums:
                return render(request, 'game.html', {'error': "numbers must be different"})
            else:
                user_nums.append(int(request.POST.get(f'number{i}')))
                if user_nums[-1] in numbers:
                    if user_nums[-1]==numbers[i-1]:
                        bulls += 1
                    else:
                        cows += 1
        print(f'bulls={bulls}, cows={cows}')
        print(user_nums)