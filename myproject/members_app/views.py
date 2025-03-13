from django.shortcuts import render

def input_view(request):
    return render(request, 'members/input.html')

def display_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        return render(request, 'members/display.html', {'username': username})
    return render(request, 'members/input.html')

def session_view(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    return render(request, 'members/session.html', {'counter': request.session['counter']})

