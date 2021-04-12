from django.shortcuts import render,redirect


def index(request):
    if 'refresh_counter' in request.session:
        request.session['refresh_counter'] = int(request.session['refresh_counter']) + 1
    else:
        request.session['refresh_counter'] = 0
    if 'counter' in request.session:
        request.session['counter'] = int(request.session['counter']) + 1
    else:
        request.session['counter'] = 0
    return render(request,"index.html")


def destroy(request):
    del request.session['counter']
    del request.session['refresh_counter']
    return redirect('/')


def add_two(request):
    request.session['counter'] = int(request.session['counter']) + 1
    return redirect('/')


def add_value(request):
    print("value is :",request.POST['increment_value'])
    input_val = request.POST['increment_value']
    request.session['counter'] = int(request.session['counter']) + int(input_val) - 1
    return redirect('/')