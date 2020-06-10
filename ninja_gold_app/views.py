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
    if 'totalGold' not in request.session:
        request.session['totalGold'] = 0
    if 'activitylog' not in request.session:
        request.session['activitylog'] = []

    # if 'time_log' not in request.session:
    #     request.session['time_log'] = []

    return render(request, "index.html", context)

def process(request):
    print('************')
    print(f"welcome to the: {request.POST['location']} ")
    print('************')
    
    # FARM
    if request.POST['location'] == 'farm':
        goldearned = random.randint(5,10)
        request.session['totalGold'] += goldearned
        #print(f"went to farm and earned {goldearned}")
        activityString = f"went to farm and earned {goldearned}"
        request.session['activitylog'].append(activityString)




        # request.session['time_log'] += goldearned
        # request.session['time_log'].append(activityString)




        
    # CAVE
    elif request.POST['location'] == 'cave':
        goldearned = random.randint(15,25)
        request.session['totalGold'] += goldearned
        if goldearned < 0:
            #print(f"went to cave and lost {abs(goldearned)}")
            activityString = f"went to cave and lost {abs(goldearned)}"
            request.session['activitylog'].append(activityString)
        else:
            #print(f"went to cave and earned {goldearned}")
            activityString = f"went to cave and earned {goldearned}"
            request.session['activitylog'].append(activityString)

    # HOUSE
    elif request.POST['location'] == 'house':
        goldearned = random.randint(-25,10)
        request.session['totalGold'] += goldearned
        if goldearned < 0:
            activityString = f"went to old house and lost {abs(goldearned)}"
            request.session['activitylog'].append(activityString)
        else:
            activityString = f"went to old house and earned {goldearned}"
            request.session['activitylog'].append(activityString)

    # CASINO
    elif request.POST['location'] == 'casino':
        goldearned = random.randint(-50,50)
        request.session['totalGold'] += goldearned
        if goldearned < 0:
            activityString = f"went to casino and lost {abs(goldearned)}"
            request.session['activitylog'].append(activityString)
        else:
            
            activityString = f"went to casino and earned {goldearned}"
            request.session['activitylog'].append(activityString)

    if request.session['totalGold'] < 0:
        activityString = f"YOU LOST IT ALL !"

    return redirect("/")

#RESET BUTTON            
def reset(request):
    del request.session['activitylog']
    del request.session['totalGold']
    return redirect("/")