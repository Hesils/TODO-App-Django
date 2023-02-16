from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from tasks.models import User, Categorie, Task

def index(request):
    if not 'user' in request.session:
        return redirect(login)
    context = {}
    context["user"] = request.session["user"]
    context['categories'] = Categorie.objects.filter(user=context["user"]["pk"]).order_by("name")
    categorie_pk = request.GET.get("categorie_pk")
    categorie = Categorie.get_default_categorie(User.objects.get(pk=context["user"]["pk"]))
    if categorie_pk:
        categorie = get_object_or_404(Categorie, pk=categorie_pk, user=User.objects.get(pk=context["user"]["pk"]))
    context['tasks'] = categorie.task_set.all()
    context["active_categorie"] = categorie
    return render(request, 'tasks/index.html', context=context)

"""---------Categories views--------"""
def add_categorie(request):
    name = request.POST.get('categorie_name')
    # default user:
    user = User.objects.get(username=request.session["user"]["username"])
    categorie, created = Categorie.objects.get_or_create(name=name, user=user)
    if not created:
        return HttpResponse("La categorie existe deja.", status=409)
    return render(request, 'tasks/categories.html', context={'categorie': categorie})

def delete_categorie(request, categorie_pk):
    categorie = get_object_or_404(Categorie, pk=categorie_pk)
    categorie.delete()
    return redirect('home')

"""---------Tasks views--------"""
def add_task(request):
    name = request.POST.get('task_name')
    description = request.POST.get('task_description')
    user = User.objects.get(pk=request.session["user"]["pk"])
    categorie = Categorie.get_default_categorie(user)
    categorie_pk = request.POST.get("categorie")
    if categorie_pk:
        categorie = Categorie.objects.get(pk=categorie_pk)
    task = Task.objects.create(name=name, description=description, categorie=categorie, user=user)
    return render(request, 'tasks/task.html', context={'task': task, "categorie": categorie})

def get_tasks(request, categorie_pk):
    categorie = get_object_or_404(Categorie, pk=categorie_pk)
    tasks = categorie.task_set.order_by("name")
    return render(request, 'tasks/tasks.html', context={"tasks": tasks, "categorie": categorie})

def delete_task(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.delete()
    return HttpResponse("")

"""---------User views--------"""

def login(request):
    context = {}
    if 'user' in request.session:
        return redirect(index)
    if 'usernameerror' in request.session:
        context["usernameerror"] = True
        del request.session['usernameerror']
    if 'usernamemissing' in request.session:
        context["usernamemissing"] = True
        del request.session['usernamemissing']
    if 'passwordmissing' in request.session:
        context["passwordmissing"] = True
        del request.session['passwordmissing']
    if 'invalidcombinaison' in request.session:
        context["invalidcombinaison"] = True
        del request.session["invalidcombinaison"]
    if 'user_name' in request.session:
        context["user_name"] = request.session['user_name']
        del request.session["user_name"]
    if 'user_password' in request.session:
        context["user_password"] = request.session['user_password']
        del request.session["user_password"]
    return render(request, "users/index.html", context=context)

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('login_page')

def sign_up(request):
    context = {}
    if 'usernamemissing' in request.session:
        context['usernamemissing'] = True
        del request.session["usernamemissing"]
    if 'passwordmissing' in request.session:
        context['passwordmissing'] = True
        del request.session["passwordmissing"]
    if 'emailmissing' in request.session:
        context['emailmissing'] = True
        del request.session["emailmissing"]
    if 'usernameused' in request.session:
        context['usernameused'] = True
        del request.session["usernameused"]
    if 'emailused' in request.session:
        context['emailused'] = True
        del request.session["emailused"]
    if 'user_name' in request.session:
        context['user_name'] = request.session["user_name"]
        del request.session["user_name"]
    if 'user_password' in request.session:
        context['user_password'] = request.session["user_password"]
        del request.session["user_password"]
    if 'user_mail' in request.session:
        context['user_mail'] = request.session["user_mail"]
        del request.session["user_mail"]
    return render(request, "users/signup.html", context=context)

def sign_in(request):
    username = request.POST.get("username")
    request.session['user_name'] = username
    password = request.POST.get("password")
    request.session['user_password'] = password
    if username == "" or password == "":
        if username == "":
            request.session['usernamemissing'] = True
        if password == "":
            request.session['passwordmissing'] = True
        return redirect(login)
    users = User.objects.all()
    user = None
    for obj in users:
        if obj.username == username:
            if obj.password == password:
                user = obj
                break
            else:
                request.session["invalidcombinaison"] = True
                return redirect(login)
    if not user:
        request.session['usernameerror'] = True
        return redirect(login)
    user_dict = {'username': user.username, 'pk': user.pk}
    request.session['user'] = user_dict
    return redirect(index)

def add_user(request):
    user_name = request.POST.get("user_name")
    request.session["user_name"] = user_name
    user_password = request.POST.get("user_password")
    request.session["user_password"] = user_password
    user_mail = request.POST.get("user_mail")
    request.session["user_mail"] = user_mail
    users = User.objects.all()
    if user_name == "" or user_password == "" or user_mail == "":
        if user_name == "":
            request.session["usernamemissing"] = True
        if user_password == "":
            request.session["passwordmissing"] = True
        if user_mail == "":
            request.session["emailmissing"] = True
        return redirect(sign_up)
    for user in users:
        if user.username == user_name:
            request.session["usernameused"] = True
            return redirect(sign_up)
        elif user.email == user_mail:
            request.session["emailused"] = True
            return redirect(sign_up)
    User.objects.create(username=user_name, password=user_password, email=user_mail)
    return redirect(login)