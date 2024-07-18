from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == username and password == password:
            request.session['username'] = username
            print("Session created: ", request.session.get('username'))  
            username_n = request.session.get('username')
            return redirect('home')
        else:
            return render(request, 'session/login.html', {'error': 'Invalid credentials'})
    return render(request, 'session/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

def home_view(request):
    if not request.session.session_key:
        return redirect('login')
    else:
        username_n = request.session.get('username')
        return render(request, 'session/home.html',{'username': username_n})

    # return render(request, 'session/home.html')