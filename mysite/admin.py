from django.contrib import admin
from .models import Produto, LivroVisitas, Projetos

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'artista', 'descricao', 'preco', 'foto', 'criado', 'modificado', 'slug')

@admin.register(LivroVisitas)
class LivroVisitasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado')

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'imagem', 'link', 'criado')

# Register your models here.
