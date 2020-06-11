from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
from datetime import datetime
import random

def index(request):
    now = datetime.now()
    print(now)
    context = {
        'current_time': now
        
    }
    #totalGold = is a cookie stored in dict
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []
    return render(request, "index.html", context)

def process(request):
    print('************')
    print(f"welcome to the: {request.POST['location']} ")
    print('************')

    def win():
            activityString = f"⚔ Good job ! you won 200 gold coins !!! ⚔"
            request.session['activity_log'].append(activityString)
            reset_scores(request)
    
    def lost():
            print(f"\033[0;37;45m game over   ")   
            print(f"score : {goldearned}")
            print(f"score total: {request.session['total_gold']} ")      
            activityString = f"☠ You lost all your gold. GAME OVER ☠"                                           
            request.session['activity_log'].append(activityString)
            reset_scores(request)
            

    # FARM
    if request.POST['location'] == 'farm':
        goldearned = random.randint(5,10)
        request.session['total_gold'] += goldearned
        activityString = f"went to farm and earned {goldearned}"
        request.session['activity_log'].append(activityString)

        if request.session['total_gold'] >= 200:
            win()


    # CAVE
    elif request.POST['location'] == 'cave':
        goldearned = random.randint(15,25)
        request.session['total_gold'] += goldearned
        activityString = f"went to cave and earned {goldearned}"
        request.session['activity_log'].append(activityString)
        
        if request.session['total_gold'] >= 200:
            win()

    # HOUSE
    elif request.POST['location'] == 'house':
        goldearned = random.randint(-25,10)
        request.session['total_gold'] += goldearned
        if goldearned < 0:
            activityString = f"went to old house and lost {abs(goldearned)}"
            request.session['activity_log'].append(activityString)

            if request.session['total_gold'] <= 0:
                lost()

        else:
            activityString = f"went to old house and earned {goldearned}"
            request.session['activity_log'].append(activityString)
            if request.session['total_gold'] >= 200:
                win()

    # CASINO
    elif request.POST['location'] == 'casino':
        goldearned = random.randint(-50,50)
        request.session['total_gold'] += goldearned
        if goldearned < 0:
            activityString = f"went to casino and lost {abs(goldearned)}"
            request.session['activity_log'].append(activityString)
            if request.session['total_gold'] <= 0:
                lost()
        else:
            activityString = f"went to casino and earned {goldearned}"
            request.session['activity_log'].append(activityString)
            if request.session['total_gold'] >= 200:
                win()

    return redirect("/")

#RESET BUTTON            
def reset_all(request):
    del request.session['activity_log']
    del request.session['total_gold']
    return redirect("/")

def reset_scores(request):
    del request.session['total_gold']
    return redirect("/")

