from django.shortcuts import render, redirect
import random


def index(request):
    if 'score_history' in request.session:
        pass
    else:
        request.session['score_history'] = [
            {"first":1},
            {"second":2},
            {"third":3},
            {"fourth":4},
            {"fifth":5},
        ]

    if 'hidden_number' in request.session:
        pass
    else:
        request.session['hidden_number'] = random.randint(1, 100)
        request.session['game_status'] = "new"
        request.session['remaining_guesses'] = 5

    context = {
        "guess_count": 5 - int(request.session['remaining_guesses']),

    }
    return render(request,"index.html", context)


def guess(request):
    print(request.POST['player_guess'])
    print(request.session['hidden_number'])
    if int(request.POST['player_guess']) > int(request.session['hidden_number']):
        request.session['game_status'] = "high"
    elif int(request.POST['player_guess']) < int(request.session['hidden_number']):
        request.session['game_status'] = "low"
    else:
        request.session['game_status'] = "won"
        return redirect("/")
    request.session['remaining_guesses'] = int(request.session['remaining_guesses']) - 1
    if int(request.session['remaining_guesses']) < 1:
        request.session['game_status'] = "lost"
    return redirect("/")


def high_score(request):
    for index in range (len(request.session['score_history'])-1, -1, -1):
        for key in request.session['score_history'][index]:
            if int(request.session['remaining_guesses']) < int(request.session['score_history'][index][key]):
                for over_write in range (len(request.session['score_history'])-2, index, -1):
                    request.session['score_history'][over_write + 1 ] = request.session['score_history'][over_write]
                request.session['score_history'][index] = {request.POST["high_score_input"]: request.session['remaining_guesses']}
                break
    request.session.save()
    return redirect("/reset")


def reset(request):
    del request.session['hidden_number']
    del request.session['game_status']
    del request.session['remaining_guesses']
    return redirect("/")