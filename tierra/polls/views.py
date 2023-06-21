from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

# Create your views here.


def login(request):
     return render(request, "logup.html")

def authenticate(request):   
    userName = request.POST['name']
    password = request.POST['password']
    user= Users()
    authenticated = user.isAuthenticated(userName,password)
  
    if authenticated:
        request.session['user_name'] = userName
        request.session['loggedIn'] = True
        return HttpResponseRedirect("HomePage")
    else:    
        context={'message': "Usuario o contraseña incorrectos!"}
        return render(request, "logup.html", context)
# 
# 
# 
def logout(request):
    request.session['loggedIn'] = False
    return HttpResponseRedirect("/")
# 
# 
# 
def index(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:    
        usuario = request.session['user_name']
        contexto = {"usuario": usuario}
        return render(request, "homepage.html", contexto)
    else:
        return HttpResponseRedirect("/")
# 
# 
#