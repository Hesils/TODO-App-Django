from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import User

def index(request):
    return render(request, 'tasks/index.html', context={})
def add_categorie(request):
    print(request.POST)
    return redirect(index)

def login(request):
    return HttpResponse("<h1>Login Page</h1>")

def sign_up(request):
    return render(request, "users/index.html", context={})

def add_user(request):
    user_name = request.POST.get("user_name")
    user_password = request.POST.get("user_password")
    user_mail = request.POST.get("user_mail")
    users = User.objects.all()
    print(f"user in fb : {users}")
    print(f"username : {user_name}\nuser password : {user_password}\nuser_mail : {user_mail}")
    if user_name == "" or user_password == "" or user_mail == "":
        return redirect(sign_up)
    for user in users:
        if user.username == user_name:
           return redirect(sign_up)
    User.objects.create(username=user_name, password=user_password, email=user_mail)
    return redirect(login)