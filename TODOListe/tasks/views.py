from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import User, Categorie, Task

def index(request):
    if not 'user' in request.session:
        return redirect(login)
    context = {}
    context["user"] = request.session["user"]
    context['categories'] = Categorie.objects.order_by("name")
    return render(request, 'tasks/index.html', context=context)

def add_categorie(request):
    name = request.POST.get('categorie_name')
    # default user:
    user = User.objects.last()
    categorie, created = Categorie.objects.get_or_create(name=name, user=user)
    if not created:
        return HttpResponse("La categorie existe deja.", status=409)
    return HttpResponse(f"<h2>{name}</h2>")

def login(request):
    return render(request, "users/index.html", context={})

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return render(request, "users/index.html", context={})

def sign_up(request):
    return render(request, "users/signup.html", context={})

def sign_in(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    users = User.objects.all()
    user = None
    for obj in users:
        if obj.username == username:
            if obj.password == password:
                user = obj
                break
            else:
                return HttpResponse("Informations ne correspondent pas", status=409)
    if not user:
        return HttpResponse("Utilisateur inconnu", status=409)
    user_dict = {'username': user.username, 'pk': user.pk}
    request.session['user'] = user_dict
    return redirect(index)
    # return render(request, "users/signup.html", context={})

def add_user(request):
    user_name = request.POST.get("user_name")
    user_password = request.POST.get("user_password")
    user_mail = request.POST.get("user_mail")
    users = User.objects.all()
    if user_name == "" or user_password == "" or user_mail == "":
        return HttpResponse("Informations manquantes", status=409)
    for user in users:
        if user.username == user_name:
            return HttpResponse("Ce nom d'utilisateur est déjà pris.", status=409)
    User.objects.create(username=user_name, password=user_password, email=user_mail)
    return redirect(login)