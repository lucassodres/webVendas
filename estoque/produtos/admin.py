from django.contrib import admin
from .models import Produtos
from .models import TabelaPrecos
from .models import PrecosPomocionais
from .models import ImagensProdutos


admin.site.register(Produtos)
admin.site.register(TabelaPrecos)
admin.site.register(PrecosPomocionais)
admin.site.register(ImagensProdutos)
