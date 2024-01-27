from django.contrib import admin
from .models import Estabelecimento, Cidade, Categoria, subCategoria, Imagem


@admin.register(Estabelecimento)
class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'categoria', 'subCategoria')
    list_editable = ('cidade', 'categoria')
    list_filter = ('nome', 'cidade')
    prepopulated_fields = {"slug": ("nome",)}  # new
    
admin.site.register(Cidade)
admin.site.register(Categoria)
admin.site.register(subCategoria)
admin.site.register(Imagem)