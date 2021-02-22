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
    return render(request, 'home.html',{'win':False})

def game(request):
    global win
    win = False
    if request.method=="GET":
        return render(request,'game.html')
    elif request.method =="POST":
        user_nums = []
        cows = 0
        bulls = 0
        try:
            for i in range(1,5):
                number = int(request.POST.get(f'number{i}'))
                if number in user_nums:
                    return render(request, 'game.html', {'error': "numbers must be different!"})
                elif number>10 or number<1:
                    return render(request, 'game.html', {'error': "numbers must be between 1 and 10!"})
                else:
                    user_nums.append(number)
                    if user_nums[-1] in numbers:
                        if user_nums[-1]==numbers[i-1]:
                            bulls += 1
                        else:
                            cows += 1
        except:
            return render(request, 'game.html', {'error': "Enter correct numbers!"})
        if bulls!=4:
            return render(request, 'game.html', {'continue':True, 'bulls':bulls, 'cows':cows})
        else:
            set_numbers()
            print(numbers)
            return  render(request, 'home.html', {'win':True})