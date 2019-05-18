from django.contrib import admin
from .models import Usuarios
from .models import Permissoes

admin.site.register(Usuarios)
admin.site.register(Permissoes)

