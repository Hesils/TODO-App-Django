from django.contrib import admin
from tasks.models import Categorie, Task, User
# Register your models here.
admin.site.register(User)
admin.site.register(Categorie)
admin.site.register(Task)