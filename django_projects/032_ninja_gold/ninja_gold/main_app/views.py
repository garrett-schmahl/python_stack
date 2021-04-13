from django.shortcuts import render, redirect
import random
from time import localtime, strftime

# Create your views here.
def index (request):
    if "game_state" in request.session:
        pass
    else:
        request.session['game_state'] = 'new'
        request.session['player_gold'] = 0
        request.session['activity_log'] = []
    return render(request, 'index.html')

def process(request):
    if request.POST['player_action'] == 'farm':
        goldmin = 10
        goldmax = 20
    elif request.POST['player_action'] == 'cave':
        goldmin = 5
        goldmax = 10
    elif request.POST['player_action'] == 'house':
        goldmin = 2
        goldmax = 5  
    elif request.POST['player_action'] == 'casino':
        goldmin = -50
        goldmax = 50  
    gold_gain = random.randint(goldmin, goldmax)
    request.session['player_gold'] += gold_gain
    if gold_gain > -1:
        gain_string = "Earned"
    else:
        gain_string = "Lost"
    current_time = strftime("%Y/%d/%m %I:%M %p", localtime())
    request.session['activity_log'].append(f"{gain_string} {gold_gain} gold from the {request.POST['player_action']} ({current_time})")
    return redirect('/')
